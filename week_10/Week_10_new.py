# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:52:44 2021

@author: ajaz7
"""
#=============================================================================
##### BINARY TREES #########
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def add_child(self, data): ## method to add a child to the tree
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left = self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right = self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        ## update height of self and thereby recursively all nodes called
        self.height = self.node_height()
        if    self.balance_factor() == 2 and self.left.balance_factor() == 1:
            self = self.LL_rotation()
        elif  self.balance_factor() == 2 and self.left.balance_factor() == -1:
            self = self.LR_rotation()
        elif self.balance_factor() == -2 and self.right.balance_factor() == -1:
            self = self.RR_rotation()
        elif self.balance_factor() == -2 and self.right.balance_factor() == 1:
            self = self.RL_rotation()
        
        return self

    def node_height(self):
        h_left=0;  h_right=0
        if self:
            if self.left:
                h_left = self.left.height
            if self.right:
                h_right = self.right.height
        return(max([h_left, h_right]) + 1)
                
    def balance_factor(self):
        h_left=0; h_right=0
        if self:
            if self.left:
                h_left = self.left.height
            if self.right:
                h_right = self.right.height
        return (h_left - h_right)            
        
    def LL_rotation(self):
        A = self
        B = self.left
        #consider links between these  nodes severed.    
        #Now first change existing link
        A.left = B.right
        # create the new link
        B.right = A
        #Update heights   
        A.height = A.node_height()
        B.height = B.node_height()
        return B
    
    def RR_rotation(self):
        A = self
        B = self.right
        #consider links between these two nodes severed. 
        #Now first change existing link
        A.right = B.left
        # create the new link
        B.left = A
        
        
        A.height = A.node_height()
        B.height = B.node_height()
        return B
    
    def LR_rotation(self):
        A = self
        B = self.left
        C = self.left.right
        #consider links between these three nodes severed. 
        
        #Now first change existing links 
        B.right = C.left
        A.left = C.right
        #then create creating new links
        C.left = B
        C.right = A
        
        
        B.height = B.node_height() 
        A.height = A.node_height()
        C.height = C.node_height() 
        
        return C
              
        
    def RL_rotation(self):
        A = self
        B = self.right
        C = self.right.left
        #consider links between these three nodes severed.
        #Now first change existing links 
        A.right = C.left
        B.left = C.right
        #then create creating new links
        C.left = A
        C.right = B 
        
        A.height = A.node_height() 
        A.height = B.node_height()
        C.height = C.node_height() 
        return C
        
    

        
    def in_order_traversal(self): ## method to perform in_order traversal
        elements = []
        #visit the left sub tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit the node
        elements.append(self.data)

        #visit the left sub tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements 

    def pre_order_traversal(self): ## method to perform pre_order traversal
        spaces = '  ' * (10-self.node_height())
        prefix = spaces + "|__" 
        elements = []
        print(prefix + str(self.data))
        #visit the node
        elements.append(self.data)
        #visit the left sub tree
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit the left sub tree
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    

    def search(self, val): ## method to search a value in the tree
        if self.data == val:
            return True

        if val < self.data: #value might be in left subtree
            if self.left:
                return self.left.search(val)
            else:       #end reached
                return False

        if val > self.data: #value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:      #end reached
                return False

    
    def delete(self, val):   ## method to remove a node in the tree
        #perform BST Delete
        if val < self.data:  # value is less than current node
            if self.left:
                self.left = self.left.delete(val) # set pruned subtree to as new left subtree
        elif val > self.data:  # value is greater than current node
            if self.right:
                self.right = self.right.delete(val) # set pruned subtree to as new right subtree
        else:                   # value equals current node
            if self.left is None and self.right is None: # current node has no children
                return None
            elif self.left is None:     #current node has only a right child
                return self.right
            elif self.right is None:    #current node has only a left child
                return self.left
            else:                       #current node has two children
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
        
        #find height of self
        # get lanace factor
        # apply cases

        return self
 

    def find_max(self):    ## method to find the maximum value in the tree
        if self.right is None:
            return self.data
        return self.right.find_max() # could have used a while loop too

    def find_min(self):    ## method to find the minimum value in the tree
        if self.left is None:
            return self.data
        return self.left.find_min()
    
###Lets define a function which will create our tree from a list
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root = root.add_child(elements[i])
    return root



root = BinarySearchTreeNode(20) 
root = root.add_child(15)
root = root.add_child(10)
root = root.add_child(7)
root = root.add_child(18)
#LL 20 15 10
#RR 20 25 30
#LR 20 15 17
#RL 20 30 10
root.pre_order_traversal()



numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
numbers_tree.pre_order_traversal()