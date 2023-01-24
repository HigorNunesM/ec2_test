import subprocess
import sys
import boto3

ec2 = boto3.client('ec2', region_name='eu-central-1')

ec2.terminate_instances(InstanceIds=[sys.argv[1]])
