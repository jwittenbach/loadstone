from setuptools import setup

version = '0.0.1'

setup(
    name='loadstone',
    version=version,
    description='cli to setup Thunder on a EC2 cluster with Spark setup by flintrock',
    long_description='See https://github.com/jwittenbach/loadstone',
    author='jwittenbach',
    author_email='jason.wittenbach@gmail.com',
    url='https://github.com/jwittenbach/loadstone',
    install_requires=open('requirements.txt').read().split('\n'),
    entry_points='''
        [console_scripts]
        loadstone=loadstone:cli
        '''
)
