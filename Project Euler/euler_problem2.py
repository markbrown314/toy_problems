"""
Euler Problem #2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
from math import sqrt, log10, ceil

def evenfib_iterative(limit):
    acc = 0
    fibv = 2
    fibp = 1
    temp = 0
    while (fibv <= limit):
        if (not fibv % 2):
            acc += fibv
        temp = fibp
        fibp = fibv
        fibv += temp
    return acc

if __name__ == "__main__":
    print(evenfib_iterative(4*10**6))