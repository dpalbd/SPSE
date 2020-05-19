#!/usr/bin/env python

import threading
import Queue
import time
import sys

class WorkerThread(threading.Thread):

        def __init__(self, queue):
                threading.Thread.__init__(self)
                self.queue = queue

        def run(self):
                print "In WorkerThread"

                while True:
                        user,password = self.queue.get()
                        print ("username and password combo is ") , user,password
                        self.queue.task_done()



#queue to fetch work from
queue = Queue.Queue()

for i in range(10):
        print "Creating WorkerThread : %d" %i

        #give the queue to the Workerthread
        worker = WorkerThread(queue)
        worker.setDaemon(True)
        worker.start()
        print "WorkerThread %d Created!"%i

fd=open(sys.argv[1],"r")
for line in fd.readlines():
        user,password=line.strip().split(':')
        queue.put((user,password))

queue.join()
print "All tasks are over!"
