#!/usr/bin/env python
# coding: utf-8

# In[1]:


hist_stack = []
hist_stack.append('www.aljazeera.com')
hist_stack.append('www.aljazeera.com/features')
hist_stack.append('www.aljazeera.com/economy')


# In[4]:


len(hist_stack)


# In[3]:


hist_stack.pop()


# In[5]:


hist_stack.is_empty()


# In[6]:


hist_stack[-1]


# In[22]:


class Stack:
    def __init__ (self):
        ## create an empty stack
        self.s = []
        
    def push (self, value):
        # add an element onto the stack 
        self.s.append(value)
        
    def pop (self):
        #collect the topmost element
        return self.s.pop()
        
    def size (self):
        return len(self.s)
    
    def peek (self):
        #just see the topmost element, don't collect it
        return self.s[-1]
    
    def is_empty(self):
        return (len(self.s) == 0) 


# In[23]:


my_stack = Stack()


# In[24]:


my_stack.push(3)


# In[25]:


my_stack.push(4)


# In[26]:


my_stack.push(27)


# In[27]:


my_stack.push(14)


# In[28]:


my_stack


# In[29]:


my_stack.size()


# In[30]:


my_stack.peek()


# In[31]:


my_stack.is_empty()


# In[20]:





# In[32]:


my_stack.pop()


# In[33]:


my_stack.peek()


# In[37]:


my_stack.pop()


# In[38]:


def well_balanced(expr):
    #return true if all parenthesis match properly
    left_signs = '({['
    right_signs = ')}]'
    
    signs_stack = Stack()
    for c in expr:
        if c in left_signs:
            signs_stack.push(c) # push delimiter onto the stack
        elif c in right_signs:
            if signs_stack.is_empty(): # nothing to match to in the stack
                return False #
            if right_signs.index(c) != left_signs.index(signs_stack.pop()):
                return False
    return signs_stack.is_empty()


# In[43]:


expr = '{2{3*y + 6* x}**(sqrt(3))}'
well_balanced(expr)


# In[187]:


class Queue:
    #fifo queue implementation of a list
    CAPACITY = 3
    def __init__ (self):
        #create an empty queue
        self.Q = [None] * Queue.CAPACITY
        self.SIZE = 0
        self.FRONT = 0
    
    def size (self):
        #return size of the queue  (r - f + N) mod N
        return self.SIZE
    
    def is_empty(self):
        #check if queue is empty
        return self.SIZE == 0
    
    def first(self):
        #look at the front of the queue
        if self.is_empty():
            #raise Exception('Queue is empty')
            print('Queue is empty')
            return
        return self.Q[self.FRONT]
    
    def dequeue(self):
        #remove/collect the front element from the queue
        if self.is_empty():
            #raise Exception('Queue is empty')
            print('Queue is empty')
            return
        answer = self.Q[self.FRONT]
        self.Q[self.FRONT] = None
        self.FRONT = ((self.FRONT + 1) % Queue.CAPACITY)
        self.SIZE -= 1
        return answer
    
    def enqueue(self, value):
        #add an element at the rear of the queue
        if self.size() >= Queue.CAPACITY:
            #raise Exception('Queue is Full')
            print('Queue is full')
            return
        REAR = (self.FRONT + self.SIZE)%
        self.Q[self.REAR] = value
        


# In[208]:


myQ = Queue()


# In[209]:


myQ.enqueue(37)


# In[212]:


myQ.Q


# In[201]:


myQ.FRONT


# In[202]:


myQ.REAR


# In[203]:


myQ.size()


# In[120]:


myQ.is_empty()


# In[97]:


myQ.dequeue()


# In[114]:


myQ.q


# In[243]:


class Queue:
  #FIFO queue implementation using a Python list as underlying storage
    DEFAULT_CAPACITY = 3          # moderate capacity for all new queues
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


# In[261]:


qq.data


# In[1]:


qq.enqueue(44)


# In[262]:


qq.front


# In[254]:


qq.Size()


# In[233]:


qq.size


# In[258]:


qq.dequeue()


# In[ ]:




