#!/usr/bin/env python
#Multi Thread ARP scanner, it will detect local IP and try to get ARP responds within it's subnet i.e. /24 subnet

import threading
import Queue
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

class WorkerThread(threading.Thread) :

        def __init__(self, queue, threadID) :
                threading.Thread.__init__(self)
                self.queue = queue
                self.threadID = threadID
                #print "Worker %d Thread for scanning job" %self.threadID

        def run(self) :

                while True :

                        try :
                                ip = self.queue.get(timeout=1)
                        except  Queue.Empty :
                               # print "Worker %d Thread exit. Scanned %d IP ..." % (self.threadID, IPsuffix)
                                return
                        try:
                                arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
                                arp_response = srp1(arp_request, timeout=1, verbose=0)
                                if arp_response:
                                        print("IP: {} MAC: {}".format(arp_response.psrc, arp_response.hwsrc))
                        except :
                                        print "Error in ARP"

                        self.queue.task_done()



queue = Queue.Queue()

threads = []
for i in range(1, 10) :
        #print "Creating WorkerThread : %d"%i
        worker = WorkerThread(queue, i)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)
        #print "WorkerThread %d Created!"%i

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

print "The local machine IP is" , ip

iplist=ip.split('.')
ip_prefix = iplist[0]+'.' + iplist[1]+'.' + iplist[2] + '.'




for ip_suffix in range(1,256):
        ip = ip_prefix + str(ip_suffix)
        queue.put(ip)

queue.join()

for item in threads :
        item.join()

print "Simple Local subnet ARP Scanning Complete!"
