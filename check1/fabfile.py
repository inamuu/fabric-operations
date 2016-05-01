from fabric.api import *

def checkhost():
    run("hostname")
    run("uptime")
    run("cat /etc/redhat-release")
    run("w")
    run("sleep 5")

def resources():
    run("cat /proc/cpuinfo")
    run("free -m")
    run("sleep 10")

def iostat():
    run("iostat 1 2")
    run("sleep 10")

def disk():
    run("df -h")
    run("df -i")
    sudo("fdisk -l")
    run("sleep 10")

def login():
    sudo("last | head -5")
    sudo("lastb | head -5")

def network():
    sudo("ip -f inet a")
    sudo("route")
    run("sleep 10")

def all():
  checkhost()
  resources()
  iostat()
  disk()
  login()
  network()
