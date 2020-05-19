#!/usr/bin/python

# Understand multiple varibale in a queue
import sys
import Queue



queue=Queue.Queue()
print queue
fd=open(sys.argv[1],"r")



for line in fd.readlines():
 user,password=line.strip().split(':')
 #queue.put(([user],[password]))
# print user
# print password
 queue.put((user,password))

 #print ("queue content", (list(queue.queue)))
 #print(queue.get())
 user,password = queue.get()
# print user
 print password
