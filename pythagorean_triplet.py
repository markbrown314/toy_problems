import math

def search_for_triplet():
    a = 0
    b = 0
    c = 0
    csq = 0
    for a in range(1,1000):
        for b in range(a+1, 1000):
            csq = a**2 + b**2
            c = math.sqrt(csq)
            if c > 1000:
                break
            if a+b+c == 1000:
                return a*b*c
    print("Cannot find triplet :-(")
    return
