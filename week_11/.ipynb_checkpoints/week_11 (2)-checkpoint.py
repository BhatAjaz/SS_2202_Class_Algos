# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 06:16:09 2021

@author: ajaz7
"""
# -*- coding: utf-8 -*-
"""

@author: ajaz.bhat
"""
# a function to MERGE two sorted sub-lists in a list 

def merge (arr, low, mid, high):
    temp_arr = arr.copy()      # create a temporary list
    i, j, k = low, mid+1, low    
    
    while i <= mid and j <= high: # merge elements from two sub-lists in increasing order into the temporary list
        if arr[i] < arr[j]:
            temp_arr[k] = arr[i]  
            k += 1; i += 1
        else:
            temp_arr[k] = arr[j]
            k += 1; j += 1
            
    while i <= mid:               # add any leftover elements from first sublist to the temporary list
        temp_arr[k] = arr[i]
        k += 1; i += 1
    while j <= high:             # add any leftover elements from second sublist to the temporary list
        temp_arr[k] = arr[j]
        k += 1; j += 1
    arr = temp_arr.copy()
    print(arr)
    return arr

#my_arr = [2, 6, 8, 10, 3, 5, 9, 11]
#print(merge(my_arr,0,3,7))
        
def mergeSort_iterative (arr):
    p = 2
    while p <= len(arr):
        i = 0
        while i+p-1 < len(arr):
            low = i
            high = i + p -1
            mid = (low+high)//2
            merge(arr,low,mid,high)
            i = i + p
        p = p*2
        
    if (p/2 < len(arr)):
        merge(arr,0,p//2 - 1,len(arr)-1)
        
    return arr
        
my_arr = [16, 2, 11, 10, 4, 3]
print(mergeSort_iterative(my_arr))