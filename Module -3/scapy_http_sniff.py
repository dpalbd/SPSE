#!/usr/bin/env python

# HTTP Packet sniffer with Scapy

#https://git.hsbp.org/six/Python_2_Examples_and_Notes/src/branch/master/spse_excercises/exc_mod3_p6_sniff_http_with_scapy.py?lang=de-DE
#https://0xbharath.github.io/art-of-packet-crafting-with-scapy/scapy/sniffing/index.html
#https://scapy.readthedocs.io/en/latest/layers/http.html


#sniff(session=TCPSession, [...])

#Scapys in-built sniff() function helps us capture all traffic:
#sniff() has count, filter, iface, lfilter, prn, timeout options.
# sniff(count=4, iface='eth0')
# output = <Sniffed: TCP:0 UDP:0 ICMP:0 Other:4>
#pkts = sniff(count=1,filter="tcp and host 64.233.167.99 and port 80")



from scapy.all import *
import re
import signal


def parse_http_packet(pkt):
        pkt_raw_layer = pkt.getlayer(Raw)
        #print pkt.getlayer(Raw)
        if pkt_raw_layer is None:
                pass

        pkt_header = str(pkt_raw_layer).split('\r\n')
        for packet in pkt_header:
                if re.search("GET", packet) or re.search("POST", packet) or re.search("HTTP", packet):
                        print(packet)

def kill_program(signum,frame):
        print "Exiting the Program..."
        sys.exit(0)

signal.signal(signal.SIGINT, kill_program)
sniff(iface='eth1', filter="tcp port 80", prn=parse_http_packet)
