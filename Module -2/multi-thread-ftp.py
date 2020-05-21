#!/usr/bin/env python


from ftplib import FTP
import threading
import Queue
from termcolor import colored
from datetime import datetime


start_time = datetime.now()


class WorkerThread(threading.Thread) :

        def __init__(self, queue, threadID) :
                threading.Thread.__init__(self)
                self.queue = queue
                self.threadID = threadID
                #print "Worker %d Thread for scanning job" %self.threadID

        def run(self) :
                while True :
                        host = None
                        try :
                                host = self.queue.get(timeout=2)
                                print colored (("Try to connect FTP site" , host), 'green')
                                ftp = FTP(host)
                                ftp.login(user='anonymous', passwd = '')
                                #print ftp.retrlines('LIST')
                                ftp.retrlines('LIST')

                        except  Queue.Empty :
                                print "Worker %d Thread exit. FTP host %s..." % (self.threadID,host)
                                return

                        self.queue.task_done()


queue = Queue.Queue()

threads = []
for i in range(5) :
        #print "Creating WorkerThread : %d"%i
        worker = WorkerThread(queue, i)
        worker.setDaemon(True)
        worker.start()
        threads.append(worker)
        #print "WorkerThread %d Created!"%i

ftphostlist = ['ftp.freebsd.org', 'ftp.x.org', 'ftp.de.netbsd.org', 'ftp.redhat.com', 'ftp.gnome.org']

for host in ftphostlist :
        queue.put(host)

queue.join()

for item in threads :
        item.join()

stop_time = datetime.now()
total_time = stop_time - start_time


print colored(("[*]  Simple FTP login and print LIST complete(upto TCP 5 FTP site)! Total Duration  : %s \n" %(total_time)),'magenta')

