import subprocess

try:
 subprocess.call(["shutdown"])
except:
 subprocess.call(["sudo", "shutdown"])
