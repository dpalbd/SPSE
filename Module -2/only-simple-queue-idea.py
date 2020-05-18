#!/usr/bin/env python

# https://www.geeksforgeeks.org/queue-in-python/
# Queue is built-in module of Python which is used to implement a queue.
# queue.Queue(maxsize) initializes a variable to a maximum size of maxsize.
# A maxsize of zero '0' means a infinite queue. This Queue follows FIFO rule.

import Queue

import time

queue = Queue.Queue()

print "queue initial size"
print(queue.qsize())
time.sleep(2)

# Adding of element to queue
queue.put('a')
queue.put('b')
queue.put('c')

print ("queue content", (list(queue.queue)))


# Removing element from queue

print(queue.get())
print(queue.get())
print(queue.get())

time.sleep(1)

print ("queue content", (list(queue.queue)))

time.sleep(1)

# Return Boolean for Empty

print("Empty: ", queue.empty())
print("Full: ", queue.full())
