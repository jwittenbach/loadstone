import click
from subprocess import call 
import boto3
import botocore

def run_all(cmd, cluster):
    call('flintrock run-command ' + cluster + ' "' + cmd + '"', shell=True)

def run_master(cmd, cluster):
    call('flintrock run-command --master-only ' + cluster + ' "' + cmd + '"', shell=True)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('cluster')
def setup(cluster):
    click.echo('setting up Thunder on ' + cluster + '...\n')

    # set up security group to allow traffic for Jupyter notebook
    click.echo('configuring security group...\n')
    configure_sg()
    
    # clone the lodestone repo which contains scripts for future operations
    click.echo('downloading lodestone scripts to cluster nodes...\n')
    run_all("sudo yum -y install git", cluster)
    run_all("git clone https://github.com/jwittenbach/lodestone", cluster)

    # run the script for installation on all nodes
    click.echo('running setup scripts on cluster nodes...\n')
    run_all("bash lodestone/script_all.sh", cluster) 

@cli.command()
@click.argument('cluster')
def reboot(cluster):
    run_all('rm -rf lodestone miniconda*', cluster) 

def configure_sg():
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

if __name__ == '__main__':
    cli()
