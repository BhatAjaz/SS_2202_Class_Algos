# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:16:05 2021

@author: ajaz7
"""
class Queue:
  #FIFO queue implementation using a Python list as underlying storage
    DEFAULT_CAPACITY = 8          # moderate capacity for all new queues
    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def Size(self):
        """Return the number of elements in the queue."""
        return self.size
    
    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""

        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data[self.front]

    def dequeue(self):
        #Remove and return the first element of the queue (i.e., FIFO)
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self.data[self.front]
        self.data[self.front] = None         # help garbage collection
        self.front = (self.front + 1) % Queue.DEFAULT_CAPACITY
        self.size -= 1
        return answer

    def enqueue(self, value):
        """Add an element to the back of queue."""
        if self.size == Queue.DEFAULT_CAPACITY:
            #self._resize(2 * len(self.data))     # double the array size
            raise Exception('Queue is full')
        rear = (self.front + self.size) % Queue.DEFAULT_CAPACITY
        self.data[rear] = value
        self.size += 1
    
    def _resize(self, cap):                  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self.data                       # keep track of existing list
        self.data = [None] * cap              # allocate list with new capacity
        walk = self.front
        for k in range(self.size):            # only consider existing elements
            self.data[k] = old[walk]            # intentionally shift indices
            walk = (1 + walk) % len(old)         # use old size as modulus
            self.front = 0                        # front has been realigned

    def reversal(self, wrd):
        for i in range (len(wrd)):
            self.enqueue(wrd[i])
        rear = (self.front + self.size) % Queue.DEFAULT_CAPACITY
        for i in range (len(wrd)):
            self.front = (rear-i-1)% Queue.DEFAULT_CAPACITY
            x = qq.dequeue()
            print(x)
        self.front -=1

# In[244]:


qq = Queue()


qq.data

wrd ='stressed'
for i in range (len(wrd)):
    qq.enqueue(wrd[i])

for i in range (len(wrd)):
    qq.dequeue()
