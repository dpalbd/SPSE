#Packet injection with RAW socket



#!/usr/bin/python

import socket
import struct

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))


# Assign interface - packet sniffing and then perform injection
rawSocket.bind(("eth0", socket.htons(0x0806)))


# create a ethernet packet

# layer 2 
# src mac / dst mac / eth type
# arpaket = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x60') # 
#ARP --> dst mac / src mac / typ = 6 + 6+ 2 =14 bytes
# Good Reference - https://www.netometer.com/qa/arp.html

packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06')


## inject a string after the header
rawSocket.send(packet + "Hello There")




====================================================================================================================================

OUTPUT



tcpdump -i eth0 -vv -XX "arp"
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
12:21:04.943699 [|ARP]
        0x0000:  4865 6c6c 6f20 5468 6572 65              Hello.There
        0x0000:  aaaa aaaa aaaa bbbb bbbb bbbb 0806 4865  ..............He
        0x0010:  6c6c 6f20 5468 6572 65                   llo.There
^C
1 packet captured
2 packets received by filter
