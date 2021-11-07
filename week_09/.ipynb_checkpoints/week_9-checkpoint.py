# -*- coding: utf-8 -*-
"""
Created on

@author: ajaz
"""
class Max_Heap:
    # initializing the constructor with arr (array that we have to convert into heap). The default value is None([])
    def __init__(self, arr=[]):
        # Initializing the heap with no elements in it
        self._heap = []
        
        # If the array by the user is not empty, push all the elements
        if arr is not None:
            for root in arr:
                self.push(root)

# push is used to insert new value to the heap
    def push(self, value):
        # Appending the value given by user at the last
        self._heap.append(value)
        # Calling the bottom_up() to ensure heap is in order.
        # here we are passing our heap 
        _bottom_up(self._heap, len(self) - 1)

# pop is used to remove top value from the heap
    def pop(self):
        if len(self._heap)!=0:         # swapping the root value with the last value.
            _swap(self._heap, len(self) - 1, 0)
        # storing the popped value in the root variable

            root = self._heap.pop()

        #Calling the top_down function to ensure that the heap is still in order 
            _top_down(self._heap, 0)
            
        else:
            root="Heap is empty"
        return root

# It tells the length of the heap
    def __len__(self):
        return len(self._heap)
# print the first element (The root)
    def peek(self):
        if len(self._heap)!=0:
            return(self._heap[0])
        else:
            return("heap is empty")


# Swaps value in heap between i and j index
def _swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# This is a private function used for traversing up the tree and ensuring that heap is in order
def _bottom_up(heap, index):
    # Finding the parent of the element
    parent_index = (index - 1) // 2
    
    # If we are already at the root node return nothing
    if parent_index < 0:
        return

    # If the current node is greater than the root node, swap them
    if heap[index] > heap[parent_index]:
        _swap(heap, index,parent_index)
    # Again call bottom_up to ensure the heap is in order
        _bottom_up(heap, parent_index)

# This is a private function which ensures heap is in order after root is popped
def _top_down(heap, index):
    child_index = 2 * index + 1
    # If we are at the end of the heap, return nothing
    if child_index >= len(heap):
        return

    # For two children swap with the larger one
    if child_index + 1 < len(heap) and heap[child_index] < heap[child_index + 1]:
        child_index += 1

    # If the child node is smaller than the current node, swap them
    if heap[child_index] > heap[index]:
        _swap(heap, child_index, index)
        _top_down(heap, child_index)
        

## Making the object of the Heap class and passing the array to convert into heap
a =[1,2,3,4,5,6] 
m = Max_Heap(a)
# Checking the value at top
print("Value at top:",m.peek())
# pushing elements into heap
m.push(1)
m.push(11)
print("Value at top:",m.peek())
# Deleting the root node
print("Root popped:",m.pop())
m.push(7)
m.push(9)
m.push(15)
print("Value at top:",m.peek())
print("Root popped:",m.pop())

m2=Max_Heap([50,20,30,10,8,16])
m2.push(77)
print("Root popped:",m.pop())




def heapsort(arr):
    barr =[]
    m = Max_Heap()
    for elem in arr:
        m.push(elem)
    for i in range(len(arr)):
        barr.append(m.pop()) 
    return barr

print(heapsort([7,2,8,11,30,22]))
                 