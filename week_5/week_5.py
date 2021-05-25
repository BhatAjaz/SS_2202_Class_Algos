# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:00:36 2021

@author: ajaz7
"""
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data): ## method to add a child to the tree
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


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


    
    
    def delete(self, val):   ## method to remove a node in the tree
        #print(self.data)
        if val < self.data:  # value is less than current node
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:  # value is greater than current node
            if self.right:
                self.right = self.right.delete(val)
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

        return self

    def find_max(self):    ## method to find the maximum value in the tree
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):    ## method to find the minimum value in the tree
        if self.left is None:
            return self.data
        return self.left.find_min()
    


###Lets define a function which will create our tree from a list
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


# Lets test our tree class operations
if __name__ == '__main__':
    
    numbers_tree = build_tree([17])
    print(numbers_tree.in_order_traversal())
    numbers_tree = numbers_tree.delete(17)
    print(numbers_tree.in_order_traversal())
    
    
    
    countries = ["Brunei","Kashmir","Greece", "Italy","China","Brunei","UK","Italy"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    country_tree.in_order_traversal()
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]