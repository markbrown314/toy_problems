import timeit
from triangular import count_factors
from triangular import gen_triangular_number
from primes import Primes

i = 1

while True:
    i +=1
    pobj = Primes(i)
    t = gen_triangular_number(i)
    factors = count_factors(pobj, t)
    if factors >= 500:
        print ("factors", factors, "t", t)
        break
