"""
multiplicative persistence from Numberphile: https://www.youtube.com/watch?v=Wim9WJeDTHQ
From wikipedia: In mathematics, the persistence of a number is the
number of times one must apply a given operation to an integer before
reaching a fixed point at which the operation no longer alters the number.
"""

def multi_persist(n, iteration):

    print(iteration, ": ", n)
 
    if n < 10:
        return

    iteration += 1
    
    digits = [int(i) for i in str(n)]
    result = 1

    for i in digits:
        result *= i

    multi_persist(result, iteration)

# OEIS A003001
for i in [0, 10, 25, 39, 77, 679, 6788, 68889, 2677889, 26888999, 3778888999, 277777788888899]:
    print("n =", i)
    multi_persist(i, 0)
