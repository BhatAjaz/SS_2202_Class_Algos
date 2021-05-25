# -*- coding: utf-8 -*-
"""

@author: ajaz.bhat
"""
# a function to MERGE two sorted sub-lists in a list 

def merge (arr, low, mid, high):
    temp_arr = arr.copy()      # create a temporary list
    i, j, k = low, mid+1, low    
    
    while i <= mid and j <= high: # merge elements from two sub-lists in increasing order into the temporary list
        if temp_arr[i] < temp_arr[j]:
            arr[k] = temp_arr[i]  
            k += 1; i += 1
        else:
            arr[k] = temp_arr[j]
            k += 1; j += 1
            
    while i <= mid:               # add any leftover elements from first sublist to the temporary list
        arr[k] = temp_arr[i]
        k += 1; i += 1
    while j <= high:             # add any leftover elements from second sublist to the temporary list
        arr[k] = temp_arr[j]
        k += 1; j += 1
    print(arr)
    #return arr

#my_arr = [2, 6, 8, 10, 3, 5, 9, 11]
#print(merge(my_arr,0,3,7))
        
def mergeSort_iterative (arr):
    import math
    sort_pass = 1; sublist_id = 0; n= len(arr)
    while sort_pass <=  math.ceil(math.log2(n)):
        print(sort_pass)
        sublist_id=0
        while sublist_id < n//(2**sort_pass):
            low  = sublist_id * (2**sort_pass)
            high = low + (2**sort_pass) - 1
            mid  = (low + high)//2
            merge (arr, low, mid, high)
            sublist_id += 1
            
        # if n//(2**sort_pass) < n/(2**sort_pass):
        #      low  = 0
        #      high = n-1
        #      mid  = n//(2**sort_pass)
        #      merge (arr, low, mid, high)
            
        sort_pass += 1       
    return arr

def mergeSort_recursive(arr, low, high):
    if low < high:
        mid  = (low + high)//2
        mergeSort_recursive(arr, low, mid) # sort the left half
        mergeSort_recursive(arr, mid+1, high) #sort the right half
        merge(arr, low, mid, high)
        return arr
  
my_arr = [16, 2, 11, 4, 7]        
#my_arr = [16, 2, 11, 10, 4, 3, 7, 1]
print(mergeSort_iterative(my_arr))
#print(mergeSort_recursive(my_arr, 0, len(my_arr)-1 ))