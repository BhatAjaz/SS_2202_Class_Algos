## Create a single node.  
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
just_a_node = Node('goose')

## A linked list will be a collection of such nodes

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_node(self, data, location = 'start'):
        new_node = Node(data)
        
        if (self.head is None):
            self.head = new_node
            self.tail = new_node         
            
        else: 
            if (location == 'start'):  ##same as stack
                new_node.next = self.head
                self.head = new_node
                
            if (location == 'end'):
                # current_node = self.head
                # while (current_node.next):
                #     current_node = current_node.next
                # current_node.next = new_node
                self.tail.next = new_node
                self.tail = new_node
        self.size += 1
                
    def get_length(self):
        # if (self.head is None):
        #     print('LinkedList is Empty')
        #     return
        
        # current_node = self.head
        # counter = 0
        # while (current_node):
        #     counter+=1
        #     current_node = current_node.next
            
        # print('Length is ', counter)
        # return counter
        return self.size
        
    def delete_node(self, location = 'start'): 
        if (self.head is None):
            print('LinkedList is Empty, Nothing to delete from')
            return
        
        if (location == 'start'):
            self.head = self.head.next ##same as stack
            
        elif (location == 'end'):
                current_node = self.head
                while (current_node.next is not self.tail):
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            
            
    def printLL (self):
        if (self.head is None):
            print('LinkedList is Empty')
            return
        current_node = self.head
        list_names = ''
        while (current_node):
            list_names += str(current_node.data) + '---> '
            current_node = current_node.next
        print(list_names)

myLL = LinkedList()

myLL.insert_node('lion','start')
myLL.insert_node('goose','start')
myLL.insert_node('frog','start')
myLL.insert_node('zebra','start')

myLL.printLL()

myLL.get_length()

myLL.delete_node(location = 'end')

myLL.printLL()
myLL.get_length()

## create a stack based on linked lists

class Stack:
    def __init__ (self):
        ## create an empty stack
        self.s = LinkedList()
        
    def push (self, value):
        # add an element onto the stack 
        self.s.insert_node(value,'start')
        
        
    def pop (self):
        #collect the topmost element
        return self.s.delete_node('start')
    
    def printStack(self):
        self.s.printLL()

myStack = Stack()
myStack.push(9)
myStack.push(8)
myStack.push(7)
myStack.printStack()
myStack.pop()


## create a queue based on linked lists
class Queue:
    def __init__ (self):
        ## create an empty queue
        self.s = LinkedList()
        
    def enqueue (self, value):
        # add an element onto the stack 
        self.s.insert_node(value,'end')
        
        
    def dequeue (self):
        #collect the topmost element
        return self.s.delete_node('start')
    
    def printQueue(self):
        self.s.printLL()

myQueue = Queue()
myQueue.enqueue('Syafiq')
myQueue.enqueue('Iffah')
myQueue.enqueue('Amir')
myQueue.printQueue()
myQueue.dequeue()






# A single node of a doubly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None, prev = None): 
    self.data = data
    self.next = next
    self.prev = prev


try_this_node = Node(10)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_node (self, data, location = 'start'):
        newNode = Node(data)
        
        if (self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            if (location is 'start'):
                current_node = self.head
                newNode.next = current_node
                newNode.prev = None
                current_node.prev = newNode
                self.head = newNode
                
            if (location is 'end'): 
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
    
    #add a node between two elements
   
    #delete a node## take inspiration from the singly linked list

    
    def printLL (self):
        if (self.head is None):
            print('LinkedList is Empty')
            return
        current_node = self.head
        list_names = ''
        while (current_node):
            list_names += str(current_node.data) + '---> '
            current_node = current_node.next
        print(list_names)       
            

myDLL = DoublyLinkedList()
myDLL.insert_node(6)
myDLL.insert_node(10,'start')
myDLL.insert_node(3,'start')
myDLL.insert_node(27,'end')
myDLL.printLL()


class DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element


# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 08:14:46 2021

@author: ajaz7
"""
#############
############
# A single node of a doubly linked list
class Node:
  # constructor
  def __init__(self, data = None, prev = None, next=None): 
    self.data = data
    self.next = next
    self.prev = prev


try_this_node = Node(10)


class DoublyLinkedList:
    def __init__(self):
        """Create an empty list of nodes."""
        self.head = Node(None)         # 2 sentinels
        self.tail = Node(None)
        self.head.next = self.tail                  # trailer is after header
        self.tail.prev = self.head                  # header is before trailer
        self.size = 0                                      # number of elements
        
    def insert_node (self, data, location = 'start'):
        newNode = Node(data)
        
        ##no need to check if lift empty, bcoz sentinels exist
        if (location == 'start'):
            newNode.prev = self.head
            newNode.next = self.head.next          
            self.head.next.prev = newNode
            self.head.next = newNode
                     
        elif (location == 'end'): 
            newNode.next = self.tail
            newNode.prev = self.tail.prev    
            self.tail.prev.next = newNode
            self.tail.prev = newNode
            
        self.size += 1
 
    #delete a node## take inspiration from the singly linked list
    def delete_node(self, location = 'start'):
        """Delete nonsentinel node from the list and return it."""
        if (location == 'start'):
            uselessNode = self.head.next        
            self.head.next = uselessNode.next
            uselessNode.next.prev = self.head
            
        elif (location == 'end'): 
            uselessNode = self.tail.prev
            self.tail.prev = uselessNode.prev
            uselessNode.prev.next = self.tail
 
        return uselessNode 
 
    #add a node between two elements  
    def insert_anywhere(self, data, preceding_value, succeeding_value):
        """Add element e between two existing nodes and return new node."""
        new_node = Node(data)
        
        search_node = self.head
        while (search_node):
            if (search_node.data == preceding_value) and (search_node.next.data == succeeding_value):
                new_node.prev = search_node
                new_node.next = search_node.next
                search_node.next.prev = new_node
                search_node.next = new_node
                self.size += 1
            else:
                search_node = search_node.next
                
    def random_collector(self, steps = 1000):
        from random import randint
        for i in range(steps):
            self.insert_node(1) #all nodes have same reward of 1
        current_loc = self.head.next.next # 
        sum_reward = 0
        for trial in range(steps):
            chance = randint(1, 100)
            if chance > 99 and current_loc.next is not self.tail:
                sum_reward += int(current_loc.data)
                current_loc = current_loc.next
            elif chance < 1 and current_loc.prev is not self.head:
                sum_reward -= int(current_loc.data)
                current_loc = current_loc.prev                
        return sum_reward
    
    def printLL (self):
        if (self.head is None):
            print('LinkedList is Empty')
            return
        current_node = self.head
        list_names = ''
        while (current_node):
            list_names += str(current_node.data) + '---> '
            current_node = current_node.next
        print(list_names)       
            

myDLL = DoublyLinkedList()
myDLL.insert_node(6)
myDLL.insert_node(10,'start')
myDLL.insert_node(3,'start')
myDLL.insert_node(27,'end')
myDLL.printLL()
myDLL.delete_node('end')
myDLL.insert_anywhere(88, 10, 6)
myDLL.delete_node('start')
myDLL.printLL()

steps= 100000
reward_DLL = DoublyLinkedList()
print('Avg reward for', steps, 'steps is ', reward_DLL.random_collector(steps)/steps)
