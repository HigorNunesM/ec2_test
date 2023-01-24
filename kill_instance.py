import subprocess
import sys

instance_id = sys.argv[1]

subprocess.run(["aws", "ec2", "terminate-instances", "--instance-ids", instance_id])
