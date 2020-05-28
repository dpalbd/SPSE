# Destination MAC 
# Source MAC
# Type = ARP 



#!/usr/bin/python

import socket
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))

rawSocket.bind(("eth0", socket.htons(0x0806)))

packet = struct.pack("!6s6s2s", '\x00\x0c\x29\x8a\xa0\x68', '\x00\x0c\x29\xa9\x52\xdb', '\x08\x06')

rawSocket.send(packet + "Hello There ARP test")

print  "Length of the  packet sent:"  + str(len(packet))

=============================================================================================================================
=============================================================================================================================
=============================================================================================================================
=============================================================================================================================
=============================================================================================================================


OUTPUT


From source 
=============

tcpdump -i eth0 -vv -XX "arp"
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes

13:34:15.539222 [|ARP]
        0x0000:  4865 6c6c 6f20 5468 6572 6520 4152 5020  Hello.There.ARP.
        0x0010:  7465 7374                                test
        0x0000:  000c 298a a068 000c 29a9 52db 0806 4865  ..)..h..).R...He
        0x0010:  6c6c 6f20 5468 6572 6520 4152 5020 7465  llo.There.ARP.te
        0x0020:  7374                                     st


From destination
=================
tcpdump -i eth1 -vv -XX "arp"
tcpdump: listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes

13:34:09.116390 [|ARP]
        0x0000:  4865 6c6c 6f20 5468 6572 6520 4152 5020  Hello.There.ARP.
        0x0010:  7465 7374 0000 0000 0000 0000 0000 0000  test............
        0x0020:  0000 0000 0000 0000 0000 0000 0000       ..............
        0x0000:  000c 298a a068 000c 29a9 52db 0806 4865  ..)..h..).R...He
        0x0010:  6c6c 6f20 5468 6572 6520 4152 5020 7465  llo.There.ARP.te
        0x0020:  7374 0000 0000 0000 0000 0000 0000 0000  st..............
        0x0030:  0000 0000 0000 0000 0000 0000            ............


