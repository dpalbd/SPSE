#!/usr/bin/env python

import sys
import Queue
from threading import Thread
from termcolor import colored

queue = Queue.Queue()


def do_actual_work(queue):
 while True:
  user,password = queue.get()
  try:
   print user
   print colored (password, 'green')
  finally:
   queue.task_done()

num_of_threads = 10


for i in range(num_of_threads):
 worker = Thread(target=do_actual_work, args=(queue,))
 worker.setDaemon(True)
 worker.start()

fd=open(sys.argv[1],"r")
for line in fd.readlines():
 user,password=line.strip().split(':')
 queue.put((user,password))

queue.join()

print "All tasks are over!"

