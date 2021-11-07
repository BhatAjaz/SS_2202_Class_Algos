# -*- coding: utf-8 -*-
"""

@author: ajaz.bhat
"""
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1,0,-1):
        # Last i elements are already in place
        for j in range(n-1, n-1-i,-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j-1] :
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))
############################

def selectionSort(arr):
    n = len(arr)
    for i in range(n): 
        # Find the minimum element in remaining unsorted array from i onwards
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j             
        # Swap the found minimum element with the ith element       
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
arr = [64, 34, 25, 1112, 22, 11, 90]
print(selectionSort(arr))
####################################


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
#print(mergeSort_iterative(my_arr))
print(mergeSort_recursive(my_arr, 0, len(my_arr)-1 ))





"""
 QuickSort
 
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