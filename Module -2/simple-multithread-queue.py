#!/usr/bin/env python

# https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
# Multithreading Queues Idea


import Queue
from threading import Thread

#Define initial queue for our job

queue = Queue.Queue()

print(queue.qsize())

#Queue size '0' means a infinite queue.

# This function will fetech the data from our queue and it's associate logic and give us output.

def do_actual_work(queue):
 while True:
  print queue.get()
  queue.task_done()


# For do our job, we need to setup the worker class.
# The Queue does not have to have anything on it- it just needs to be defined so that  threads know what they will be working on.
# set '10' threads running

num_of_threads = 10


for i in range(num_of_threads):
 worker = Thread(target=do_actual_work, args=(queue,))
 worker.setDaemon(True)
 worker.start()


# Now we will define a loop provide the '20' jobs and send those to queue
 for x in range(20):
  queue.put(x)

# queue.join() at end tell us they This basically just waits until the queue is empty and all of the threads are done working
#(which it knows because task_done() will have been called on every element of the queue).

queue.join()

print "All tasks are over!"
