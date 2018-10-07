"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from primes import Primes

primes = Primes(10000)
print(list(primes.prime_factors((600851475143))))
