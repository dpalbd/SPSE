#!/usr/bin/env python
#ACK  Vivek Ramachandran :D

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
                total_ports = 0
                while True :
                        port = 0
                        try :
                                port = self.queue.get(timeout=1)
                        except  Queue.Empty :
                               # print "Worker %d Thread exit. Scanned %d ports ..." % (self.threadID, total_ports)
                                return

                        ans,unans=sr(IP(dst=sys.argv[1])/TCP(sport=RandShort(),dport=port,flags="S"),verbose=0)
                        ans.summary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA",prn=lambda(s,r):r.sprintf("%TCP.sport% is open"))

                        self.queue.task_done()
                        total_ports += 1


queue = Queue.Queue()

threads = []
for i in range(1, 10) :
        #print "Creating WorkerThread : %d"%i
        worker = WorkerThread(queue, i)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)
        #print "WorkerThread %d Created!"%i

for j in range (1024) :
        queue.put(j)

queue.join()

for item in threads :
        item.join()

print "\n Simple Scanning Complete(upto TCP port 1-1024)!"
