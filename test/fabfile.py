from fabric.api import run

def uname():
  run("uname -a")

def df():
 run("df -h")
