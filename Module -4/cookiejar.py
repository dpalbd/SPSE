#!/usr/bin/env python

#https://stackoverflow.com/questions/57350698/what-is-mechanize-cookiejar-in-mechanize-python
#https://stackoverflow.com/questions/15459217/how-to-set-cookie-in-python-mechanize

#mechanize cookiejar dvwa

from termcolor import colored
import mechanize
from bs4 import BeautifulSoup

#Create a browser object
CookieJar = mechanize.CookieJar()

br1 = mechanize.Browser()

# Cookie Jar for br1
br1.set_cookiejar(CookieJar)


#Open a webpage

print colored('Browser One','green')
response = br1.open('http://192.168.30.143/dvwa/login.php')
#print response.read()


#Submit the form with username & password

br1.select_form(nr=0)
br1.form['username'] = 'admin'
br1.form['password'] = 'password'
br1.submit()
print colored (br1.response().read(),'green')


#cookiejar
#Return the current cookiejar (mechanize.CookieJar) or None

br2 = mechanize.Browser()

#Open a webpage with CookieJar i.e. we don't need to put username/password again

print colored('Browser Two','cyan')
br2.set_cookiejar(CookieJar)
response = br2.open('http://192.168.30.143/dvwa/vulnerabilities/brute/')
#print  colored(br2.response().read(),'cyan')
soup = BeautifulSoup(br2.response().read(),'lxml')
header = soup.find_all('h1')
print  colored (header, 'cyan')
