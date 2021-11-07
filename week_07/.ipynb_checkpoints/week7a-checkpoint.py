# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:44:32 2021

@author: ajaz7
"""
##dictionaries in python
mydicto = {'20B1': 'Zara', '20B2': 'Yadin', '20B3': 'Larissa'}
print(mydicto)
print ("mydicto['20B1']: ", mydicto['20B1'])
print ("mydicto['20B3']: ", mydicto['20B3'])

mydicto['20B2'] = 'Fredo'; # update existing entry
mydicto['20B4'] = "Gurpreet"; # Add new entry

print(len(mydicto)) ## find length
del mydicto['20B3']; # remove entry with key 'Name'
mydicto.clear();     # remove all entries in dict
del mydicto ;        # delete entire dictionary


#print(mydicto)
mydicto = dict({1: 'Tom', 2: 'Dick', 3:'Harry'})

##Nested dictionary
student_info = {'20B1':{'Name' : 'Zara', 'Year' : 2019, 'Grade' : 'A+'},
                '20B2':{'Name' : 'Yadin', 'Year' : 2018, 'Grade' : 'B+'},
                '20B3':{'Name' : 'Larissa', 'Year' : 2020, 'Grade' : 'A-'}}
#print(student_info)
###
##Use of dictionaries examples
# Program to find sum of all items in a Dictionary

# Function to print sum
def returnSum(dict):    
     sum = 0
     for i in dict.values():
           sum = sum + i  
     return sum
 
# maincall
dict = {'a': 100, 'b':200, 'c':300}
print("Sum :", returnSum(dict))
'''
A program for counting word frequencies in a document, and
reporting the most frequent word. We use Python’s dict class for the map. We
convert the input to lowercase and ignore any nonalphabetic characters.
'''
freq = {}
for piece in open('mapschapter.txt').read().lower().split():
  # only consider alphabetic characters within this piece
  word = ''.join(c for c in piece if c.isalpha())
  if word:                                # require at least one alphabetic character
    freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w,c) in freq.items():    # (key, value) tuples represent (word, count)
  if c > max_count:
    max_word = w
    max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)

#################
#An example hash function which we will use later

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

get_hash('march 6')



####Hash Tables

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

myDict = HashTable()
myDict['Sept 1'] = 100
myDict['Sept 2'] = 154
print( myDict['Sept 1'] )
#print(myDict.arr)

