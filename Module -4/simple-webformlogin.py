#!/usr/bin/env python

#https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

#simple login form with username and password to DVWA

import time

from termcolor import colored

import mechanize

#Create a browser object

br = mechanize.Browser()

#Open a webpage

response = br.open('http://192.168.30.143/dvwa/login.php')
print response.read()

time.sleep(2)

#Using forms

for form in br.forms():
 print colored(form,'yellow')


time.sleep(2)


#Submit the form with username & password

br.select_form(nr=0)
br.form['username'] = 'admin'
br.form['password'] = 'password'
br.submit()
print br.response().read()



#Finding Links

for link in br.links():
 print colored(link.text,'green')
 print colored(link.url, 'cyan')
