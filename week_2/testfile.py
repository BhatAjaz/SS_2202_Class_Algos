def gcd (m,n):
    if m < n:
        (m,n) = (n,m)
    cf = 1
    for i in range(1,n+1):
        if (m%i == 0 and n%i == 0):
            cf = i
    return (cf)
gf = gcd(800000,1000000)
print ('greatest common factor is ',gf)
        
