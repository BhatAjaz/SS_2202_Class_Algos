# -*- coding: utf-8 -*-
"""


@author: ajaz
"""
def partition (arr, low, high, n):
    ## partitions the array into two adjusting pivot element at correct location 
    
    pivot =  arr[low] # choose the first element as pivot
    i = low; j = high
    
    while i<j:
        while i < n and arr[i] <= pivot: # keep moving ahead to find element larger than pivot
            i += 1       
        while j >= 0 and arr[j] > pivot: # keep moving backwards to find element smaller than pivot
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i] # exchange the large and small element positions
        
    arr[low], arr[j] = arr[j], arr[low]     # move the pivot to its correct location   
    return j



def QuickSort(arr, low, high, n):
    if low < high:
        j = partition(arr, low, high, n) # parition the array and put first element at correct location  
        QuickSort(arr, low, j, n) # quicksort the left side partition of the pivot
        QuickSort(arr, j+1, high, n) # quicksort the right side partition of the pivot

A = [11,13,7,12,16,9,100,4,23,1,24,5,10,3]
QuickSort(A, 0, len(A)-1, len(A))
print(A)