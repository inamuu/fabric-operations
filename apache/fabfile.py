from fabric.api import *

def ipcheck():
    sudo("cat /var/log/httpd/www.inamuu.com-access.log | awk '{print $1}' | sort | uniq -c | sort -n | tail -10")

def uricheck():
    sudo('cat /var/log/httpd/www.inamuu.com-access.log | awk \'$9 !~ "200|30*" {print $11}\' | sort | uniq -c | sort')
       
def all():
    ipcheck()
    uricheck()
