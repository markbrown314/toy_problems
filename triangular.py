from primes import Primes
def gen_triangular_number(x):
    return int(x*(x + 1)/2)

def count_factors(pobj, q):
    # find prime factors
    primes = list(pobj.prime_factors(q))
    #print("primes:", primes)
    factors = 1
    for (i, p) in enumerate(primes):
        n = 1
        while not q%p:
            q = int(q/p)
            n += 1
        factors = factors * n

    return factors
