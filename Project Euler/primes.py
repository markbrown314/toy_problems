from math import sqrt
from functools import reduce
import sys

class Primes:

    def __init__(self, limit):
        # prime number cache
        self.sieve = []
        self.primes = []
        self.sieve_size = 0
        self.current_prime = 0
        self.limit = limit
        self.exhausted = False

    # generate primes using sieve of eratosthenes
    def calc_primes(self, stop):
        if self.limit < 2:
            return

        if self.sieve == []:
            # create list of consecutive integers
            self.sieve = list(range(0, self.limit))
            # mark initial non prime integers
            self.sieve[0] = 0
            self.sieve[1] = 0
            self.current_prime = 2
            self.primes.append(self.current_prime)

        # select current prime
        p = self.current_prime

        # initial multiplier start at pos p^2
        n = p

        while True:
            # no more primes
            if p >= self.limit:
                self.exhausted = True
                return

            # reached stopping point
            if p >= stop:
                return

            # generate composite integer
            pos = n * p

            # reached end of current composite integer search
            if pos >= self.limit:
                # find next prime
                i = 0
                for i in range(p+1, self.limit):
                    p = 0
                    if self.sieve[i] != 0:
                        p = i
                        n = p # start at pos p^2
                        self.current_prime = p
                        self.primes.append(self.current_prime)
                        break

                # no more available prime candidates
                if p == 0 or i == 0:
                    return

                continue
            # mark composite integer as non-prime
            self.sieve[pos] = 0

            n += 1

    def gen_primes(self, limit):
        n = 0
        for i in range(2, limit):
            self.calc_primes(i)
            if len(self.primes) > n:
                for j in range(n, len(self.primes)):
                    yield(self.primes[j])
                n = len(self.primes)

    def get_primes(self):
        return self.primes

    def prime_factors(self, x):
        #print("x", x)
        self.calc_primes(x)
        #print("primes l2:", self.primes)
        for i in self.primes:
                if (not x % i):
                    yield i

    def is_exhausted(self):
        return self.exhausted

# old codebase
def is_prime(x):
    #global iters
    if (x < 2):
        return False
    if (x > 5 and (not x % 2 or not x % 3 or not x % 5)):
        return False
    for i in range (2, x-1):
            if (not x % i):
                return False
    return True

def is_mr_prime(a):
    #global iters
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        #iters = iters + 1
        if a % x == 0:
            return False
    return True

def prime_factors_brute_force(x):
    #global iters
    #iters = 0
    #niters = 0
    factors = []
    for i in range (2, int(x**0.5)):
            #niters = niters + 1
            if (not x % i):
                if (is_prime(i)):
                    factors.append(i)
    return factors

def prime_factors(x):
    #primes = primes_sieve_sof(int(x**0.5))
    primes = gen_primes_sieve_eratosthenes(int(x**0.5))
    #print("primes:", primes)
    for i in primes:
            if (not x % i):
                yield i

# integer factors
def factors(x):
    for i in prime_factors(x):
            if i**2 > x:
                continue

            j = 0
            while True:
                j += 1
                test = i*j

                if test >= (x/2)+1:
                    break

                if (not x % test):
                    yield(int(x/test))

    yield(x) # x is divisible by x
    yield(1) # 1 is divisible by x

def gen_prime(call, num):
    i = 0
    p = 0
    while True:
        i += 1
        if call(i):
            p += 1
            if num == p:
                return i
            #print(p,":[",i,"]", end='')
        #if not i%100:
            #print(".", end='')

# generate primes using sieve of eranthoses
def gen_primes_se_lt_old(num):
    if (num < 2):
        return []
    sieve=list(range(0, num))
    sieve[0] = 0
    sieve[1] = 0
    p = 2
    n = 1
    while True:
        # done
        if p >= num:
            return(sieve)

        pos = n * p
        if pos >= num:
            p += 1
            n = 1
            continue

        if (pos != p):
            sieve[pos] = 0

        n += 1

# generate primes using sieve of eranthoses
# TODO optimize by removing even numbers
def gen_primes_se_lt_old(num):
    if (num < 2):
        return []

    sieve = list(range(0, num))
    sieve[0] = 0
    sieve[1] = 0
    p = 2
    n = 1
    while True:
        # reached end of sieve
        if p >= num:
            return(list(filter(lambda x: x != 0, sieve)))

        pos = n * p
        if pos >= num:
            # find next p
            n = 1
            for i in range(p+1, num):
                p = 0
                if sieve[i] != 0:
                    p = i
                    break
            if p == 0:
                return(list(filter(lambda x: x != 0, sieve)))
            continue

        if (pos != p):
            sieve[pos] = 0

        n += 1

# generate primes using sieve of eratosthenes
def gen_primes_sieve_eratosthenes(limit):
    if (limit < 2):
        return []

    # create list of consecutive integers
    sieve = list(range(0, limit))
    # mark initial non prime integers
    sieve[0] = 0
    sieve[1] = 0
    # select initial prime
    p = 2
    # initial multiplier start at pos p^2
    n = 2

    while True:
        # no more primes
        if p >= limit:
            # filter out marked values the remainder are primes
            return(list(filter(lambda x: x != 0, sieve)))

        # generate composite integer
        pos = n * p

        # reached end of current composite integer search
        if pos >= limit:
            # find next prime
            i = 0
            for i in range(p+1, limit):
                p = 0
                if sieve[i] != 0:
                    p = i
                    n = p # start at pos p^2
                    break

            # no more available prime candidates
            if p == 0 or i == 0:
                # filter out marked values the remainder are primes
                return(list(filter(lambda x: x != 0, sieve)))

            continue
        # mark composite integer as non-prime
        sieve[pos] = 0
        n += 1

# example from stack overflow
def primes_sieve_sof(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False



def gen_prime_sum_lt(call, num):
    i = 0
    primes = []
    while True:
        i += 1
        if call(i):
            if i >= num:
                return(reduce(lambda x,y:x+y,primes))
            primes.append(i)

# generate primes using sieve of eratosthenes
def gen_primes_sieve_eratosthenes_seg(primes, start, limit):
    if (limit < 2):
        return []

    # create list of consecutive integers
    sieve = list(range(start, limit))
    # mark initial non prime integers
    sieve[0] = 0
    sieve[1] = 0
    # select initial prime
    p = 2
    # initial multiplier start at pos p^2
    n = 2

    while True:
        # no more primes
        if p >= limit:
            # filter out marked values the remainder are primes
            return(list(filter(lambda x: x != 0, sieve)))

        # generate composite integer
        pos = n * p

        # reached end of current composite integer search
        if pos >= limit:
            # find next prime
            i = 0
            for i in range(p+1, limit):
                p = 0
                if sieve[i] != 0:
                    p = i
                    n = p # start at pos p^2
                    break

            # no more available prime candidates
            if p == 0 or i == 0:
                # filter out marked values the remainder are primes
                return(list(filter(lambda x: x != 0, sieve)))

            continue
        # mark composite integer as non-prime
        sieve[pos] = 0
        n += 1
