from math import factorial

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


N = int(input())
squares = []
patterns = 0
for i in range(1, N + 1):
    tmp = prime_factorize(i ** 2)
    
