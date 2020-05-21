#https://scapy.readthedocs.io/en/latest/routing.html
#Get MAC by IP

from scapy.all import *
import sys

#mac = getmacbyip("192.168.30.143")

ip=sys.argv[1]

mac = getmacbyip(ip)
print mac
