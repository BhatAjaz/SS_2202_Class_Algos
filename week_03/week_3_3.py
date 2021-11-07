# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:31:06 2021

@author: ajaz7
"""
def revAr(A,i,j):
    if i < j:
        A[i], A[j] = A[j], A[i]
        revAr(A, i+1, j-1)
    return
A = [2,4,5,7,8,9,12]
print("Array: ",A)
revAr(A,0,6)
print("Reversed Array: ",A)


A = [2,4,15,7,18,9,12]
def finmax(A,i,curmax):
    if i > len(A)-1:
        return curmax
    else:       
        if A[i] > curmax:
            curmax = A[i]
        return finmax(A,i+1,curmax)
        
curmax = A[0]
print(finmax(A,1,curmax))


# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:01:46 2021

@author: ajaz7
"""
def even(k):
    while (k>1):
        k = k-2
    
    if k == 1:
        return False
    else:
        return True
print(even(99))


def squares(n):
    return sum([i ** 2 for i in range(n) if i%2!=0])
print(squares(6))


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
E = []
O = []
def EvenOdd(A, E, O):
    for i in range(len(A) - 1):
        if A[i] % 2 == 0:
            E.append(A[i])
        else:
            O.append(A[i])
    E.extend(O)
    return E
print ((EvenOdd(A, E, O)))

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

        

a=10
b=15
curprod = 0
def finprod(i,b):
    if i > b:
        return 0
    else:       
        return( a + finprod(i+1,b))
        
print(finprod(1,b))


def findifprime(index,num):
    if (num == 1) or (num == 2) or (num == 3):
        return True
    if index >= num:
        return True
    else:
        if num%index == 0:
            return False
        else:
            return (findifprime(index+1,num))

print(findifprime(2,31))


num =128883
rev=0
while num > 0:
    digi = num%10
    rev = rev*10 + digi
    num = num//10
print("number reversed", rev)
 


# def revnum(num,rev):
#     if num <= 0:
#         print(rev)
#         return 
#     else:
#         digi = num%10
#         rev = rev*10 + digi
#         revnum(num//10,rev)
# print(revnum(123,0))

def revnum(num,rev):
    if num <= 0:
        return rev
    else:
        digi = num%10
        rev = rev*10 + digi
        return revnum(num//10,rev)
print(revnum(6394749,0))
        

def cubroot(num, ind):
    if ind > num:
        return 0
    else: 
        if num == ind*ind*ind:
            return ind
        else:
            return cubroot(num, ind+1)
print("cube root is", cubroot(64, 1))


a=10
b=15
curprod = 0
def finprod(i,b,curprod):
    if i > b:
        return 0
    else:       
        return( a + a + finprod(i+1,b,curprod))
        
print(finprod(1,b,curprod))

def palindrom(Name,i, N):
    if i > N//2:
        return True
    else:
       if Name[i] != Name[N-1-i]:
           return False
       else:
           return palindrom(Name,i+1, N)
Name = 'maam'
N =4
print(palindrom(Name,0, N))


def palnum(Nm, num,rev):
   if num <= 0:
       return (Nm==rev)
   else:
       digi = num%10
       rev = rev*10 + digi
       return palnum(Nm, num//10,rev)
       
        
print("number is palnidrom",palnum(1221,1221,0))       
    

def recsum(N,i):
    if i>N:
        return 0
    else:
        return i + recsum(N,i+1) 
print(recsum(5,0))


def palindrome_recursive(S, start, stop):
    if start == stop:
        return True
    if S[start] != S[stop]:
        return False
    if start < stop + 1:
        palindrome_recursive(S, start+1, stop-1)
        return True

def check_palindrome(S):
    if len(S) == 0:
        return True
    return palindrome_recursive(S,0, len(S)-1)

String = "MXDAM"

if check_palindrome(String):
    print("True")
else:
    print("False")


def find_cubic(n,i):
    if (i>1):
        n = n+n
        find_cubic(n,i-1)
        return n 

print(find_cubic(2,3))

#############################
def finsqr(num,i):
    if i > num:
        return 0
    else:       
        return( num  + finsqr(num,i+1) )
    
def fincube(num):
    j = 0
    prod = 0
    while j < num:
        prod += finsqr(num,1)
        j=j+1
    return prod

num = 9
print(fincube(num))
#########
def fincube(num,j,prod):
    if j>num:
        return prod
    else:
        prod += finsqr(num,1) 
        return (fincube(num,j+1,prod)) 
num = 10
print(fincube(num,1,0))
##################################
 


def paraSA(l, b, a):
    if b != 0:
        a = a+l 
        #print (a)
        return paraSA(l,b-1,a)
    else:
        return a

print("length = 5, breadth = 6")
print ("surface area of parallelogram = ", paraSA(5,6, 0))


def findDuplicate(arr):
    arr.sort()
    return ifDuplicate(arr, 0, arr[1])

def ifDuplicate(arr, index, value):
    if index == len(arr):
        return False
    if arr[index] == value:
        return True
    return ifDuplicate(arr, index + 1, arr[index])

numberone = [5,2,5]
numbertwo = [2,3,5,7,8,2,3]

print(findDuplicate(numberone))
print(findDuplicate(numbertwo))

# -*- coding: utf-8 -*-
"""
Created on Wed May  5 22:16:05 2021

@author: ajaz7
"""
class Stack:
    def __init__(self):
        self.s=[]

    def push(self,value):
        self.s.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack empty, nothing to pop")
            return
        else:
            return self.s.pop()

    def is_empty(self):
        return len(self.s)==0

    def size(self):
        return len(self.s)

    def peek(self):
        if self.is_empty():
            print("Stack empty, nothing to pop")
            return
        else:
            return self.s[-1]

ms = Stack()
ms.push(3)
ms.push(39)
ms.push(34)
ms.push(37)
print(ms.peek())
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.pop())

class Queue:
  #FIFO queue implementation using a Python list as underlying storage
    DEFAULT_CAPACITY = 80          # moderate capacity for all new queues
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
##################

qq = Queue()


qq.data

wrd ='stressed'
for i in range (len(wrd)):
    qq.enqueue(wrd[i])

for i in range (len(wrd)):
    qq.dequeue()





####################
class DeQue:
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

    def enqueue_back(self, value):
        """Add an element to the back of queue."""
        if self.size == Queue.DEFAULT_CAPACITY:
            #self._resize(2 * len(self.data))     # double the array size
            raise Exception('Queue is full')
        rear = (self.front + self.size) % Queue.DEFAULT_CAPACITY
        self.data[rear] = value
        self.size += 1
    
    def enqueue_front(self, value):
        """Add an element to the start of queue."""
        if self.size == Queue.DEFAULT_CAPACITY:
            #self._resize(2 * len(self.data))     # double the array size
            raise Exception('Queue is full')
        self.front = (self.front - 1) % Queue.DEFAULT_CAPACITY
        self.data[self.front] = value
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


qq = DeQue()
qq.enqueue_back(10)
qq.enqueue_back(20)
qq.enqueue_back(30)
print(qq.data)
qq.enqueue_front(5)
print(qq.data)

#Show how to use a stack S and a queue Q to generate all possible subsets
#of an n-element set T nonrecursively.
n=[1,2,3,1]
st=Stack()
q=Queue()

q.enqueue(set())

for i in range(len(n)):
    st.push(n[i])


while st.is_empty()==False:
    cur_el=st.pop()
    print('cur',cur_el)
    for i in range(q.Size()):
        a=q.dequeue()
        print('dequeued now',a)
        q.enqueue(a)
        b=a|{cur_el}
        q.enqueue(b)
        print('enqueued joined',b)

while q.is_empty()==False:
    x=q.dequeue()
    print(x)

