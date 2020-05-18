#!/usr/bin/env python


#http://docs.paramiko.org/en/stable/api/client.html

import paramiko
import time

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.30.143', username='demo', password='demo123')

stdin, stdout, stderr = ssh.exec_command('cat /etc/passwd')

for line in stdout.readlines():
    print line.strip()

time.sleep(1)

stdin, stdout, stderr = ssh.exec_command('w')
print stdout.readlines()

ssh.close()
