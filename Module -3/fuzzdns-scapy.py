#!/usr/bin/env python


#https://resources.infosecinstitute.com/scapy-all-in-one-networking-tool/

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


#fuzz dns

while True:
        sr(IP(dst=sys.argv[1])/UDP()/fuzz(DNS()),inter=1,timeout=1)
