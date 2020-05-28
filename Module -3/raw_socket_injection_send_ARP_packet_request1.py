#https://www.ietf.org/proceedings/51/I-D/draft-ietf-isis-ext-eth-01.txt
#Ethernet Frame Formats
#                +----+----+------+------+-----+
#		| DA | SA | Type | Data | FCS |
#		+----+----+------+------+-----+
#
#		DA	Destination MAC Address (6 bytes)
#		SA	Source MAC Address	(6 bytes)
#		Type	Protocol Type		(2 bytes)
#		Data	Protocol Data		(46 - 1500 bytes)
#		FCS	Frame Checksum		(4 bytes)
#


# layer 2 
# src mac / dst mac / eth type
# arpaket = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x60') # 
#ARP --> dst mac / src mac / type = 6 + 6+ 2 =14 bytes
# Good Reference - https://www.netometer.com/qa/arp.html
#Type  0x0800	Internet Protocol version 4 (IPv4)
# Type 0x0806	Address Resolution Protocol (ARP)
# Type 0x8035	Reverse Address Resolution Protocol (RARP)
# Type  0x86DD	Internet Protocol Version 6 (IPv6)
# Type 0x8100	VLAN-tagged frame (IEEE 802.1Q) and Shortest Path Bridging IEEE 802.1aq with NNI compatibility
# Full reference https://en.wikipedia.org/wiki/EtherType

#Packet injection with RAW socket


#!/usr/bin/python

import socket
import struct

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))


# Assign interface - packet sniffing and then perform injection

rawSocket.bind(("eth0", socket.htons(0x0806)))


# create a ethernet packet, type IP 0x0800	Internet Protocol version 4 (IPv4)

#packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

# create a ethernet packet, type ARP Type 0x0806	Address Resolution Protocol (ARP)
 packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x06')

## inject a string after the header
rawSocket.send(packet + "Hello There")

print  "Length of the  packet sent:"  + str(len(packet))

====================================================================================================================================
====================================================================================================================================
====================================================================================================================================
====================================================================================================================================
====================================================================================================================================
====================================================================================================================================

OUTPUT

###
Length of the  packet sent:14
###

tcpdump -i eth0 -vv -XX "arp"
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
12:21:04.943699 [|ARP]
        0x0000:  4865 6c6c 6f20 5468 6572 65              Hello.There
        0x0000:  aaaa aaaa aaaa bbbb bbbb bbbb 0806 4865  ..............He
        0x0010:  6c6c 6f20 5468 6572 65                   llo.There
^C
1 packet captured
2 packets received by filter
