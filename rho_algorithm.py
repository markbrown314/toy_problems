# Pollard's rho algorithm for finding integer factorization
from math import gcd

def rho(n):
    x = 2
    y = 2
    d = 1
    g = lambda x,n: (x*x + 1) % n
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x - y), n)

    if d == n:
        return
    else:
            return d

print(rho(4000))
