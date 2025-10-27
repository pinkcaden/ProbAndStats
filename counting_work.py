import math

def trunc_fac(start, end):
    prod = 1
    for i in range(start if start < end else end ,
                   end + 1 if start < end else start + 1):
        prod *= i
    return prod

def fac(n):
    if n == 0:
        return 1
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod

def permutation(n, r):
    return trunc_fac(n, n-r + 1)

