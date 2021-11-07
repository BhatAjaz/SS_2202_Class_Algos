# -*- coding: utf-8 -*-
"""


@author: ajaz
"""
def BinarySearch(arr, key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (high - low)//2 + low
        if key == arr[mid]:
            print("found")
            return True
        elif key < arr[mid]:
            high = mid - 1
        else:
            low  = mid + 1
    print("not found")
    return False

data = [1,2,3,4]
BinarySearch(data, 3)