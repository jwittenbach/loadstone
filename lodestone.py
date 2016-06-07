import click
from subprocess import call 
import boto3
import botocore

@click.group()
def cli():
    pass 

@click.command()
@click.argument('cluster')
def setup(cluster):
    click.echo('setting up Thunder on ' + cluster + '...')
    
    # clone the lodestone repo which contains scripts for future operations
    cmd = ['flintrock', 'run-command', cluster]
    call(cmd + ["sudo yum -y install git"])
    call(cmd + ["git clone https://github.com/jwittenbach/lodestone"])

@click.command()
def sg():
    # get Flintrock security groups and make sure ports for Jupyter notebook are open
    ec2 = boto3.resource(service_name='ec2')
    for sg in ec2.security_groups.filter(Filters=[{'Name': 'group-name', 'Values': ['flintrock']}]).all():
        try:
            sg.authorize_ingress(
                IpProtocol='tcp',
                FromPort=9999,
                ToPort=9999,
                CidrIp='0.0.0.0/0')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'InvalidPermission.Duplicate':
                raise Exception('Unknown boto error when adding security group rule for Jupyter')
        try:
            sg.authorize_ingress(
                IpProtocol='tcp',
                FromPort=80,
                ToPort=80,
                CidrIp='0.0.0.0/0')
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] != 'InvalidPermission.Duplicate':
                click.echo(e.response)
                raise Exception('Unknown boto error when adding security group rule for Jupyter')

cli.add_command(setup)
cli.add_command(sg)

if __name__ == '__main__':
    cli()
