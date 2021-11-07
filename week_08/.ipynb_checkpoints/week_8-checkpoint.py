# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:00:36 2021

@author: ajaz7
"""
class TreeNode:  ## define a node in the tree, its data, parent,children, and methods,
                    ###it can be an internal node or an external node
        
    def __init__(self, data): ## initialization, fill in the node with data
        self.data = data
        self.children = []
        self.parent = None
        
    
    def add_child(self, child): ## add a child to the node
        child.parent = self
        self.children.append(child)
        return child
        
    def get_level(self):   ### find the level of a node
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):   ### print all the subtree of a node
        spaces = '   ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree() 



###Lets define a function which will create our tree with all nodes 
def build_product_tree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    phones = TreeNode("Phones")
    accessories = TreeNode("Accessories")

    root.add_child(laptops)
    root.add_child(phones)
    root.add_child(accessories)


    laptops.add_child(TreeNode("Ubuntu"))
    laptops.add_child(TreeNode("MacBook Air"))
    laptops.add_child(TreeNode("Windows"))
        
    Iphones = phones.add_child(TreeNode("iPhone"))
    phones.add_child(TreeNode("Samsung"))
    Iphones.add_child(TreeNode("12 Max"))
    
    accessories.add_child(TreeNode("Galaxy Cover"))
    

    root.print_tree()
    #print(accessories.get_level())


if __name__ == '__main__':

    ## example text create a tree node instance 
    #TreeNode("Electronics")

    
    ## Call the tree buiding function
    build_product_tree()

    
#################################
##################################
##### BINARY TREES #########
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