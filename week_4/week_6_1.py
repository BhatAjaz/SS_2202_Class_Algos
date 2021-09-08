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
