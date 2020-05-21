#!/usr/bin/env python


#https://docs.python.org/2/library/ftplib.html
#https://pythonprogramming.net/ftp-transfers-python-ftplib/



from ftplib import FTP

#domain name or server ip:

ftp = FTP('ftp.freebsd.org')
ftp.login(user='anonymous', passwd = '')
ftp.retrlines('LIST')
ftp.quit()
