def sum (A, n):
    s = 0
    for i in range(0,n):
        s = s + A[i]
    return s

Arr = [10, 13, 5, 18, 101]
n = 5
mysum = sum (Arr,5)
print(mysum)
