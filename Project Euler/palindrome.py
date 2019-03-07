import math
import primal

def reverse_number(x):
    total = 0
    while (x > 0):
        rem = x % 10
        #print("remainder of x", rem)
        total = total * 10
        total = total + rem
        x = int(x/10)
    return total

def calc():
    rev = 0
    pal = 0
    check = 0
    for i in range (999, 99, -1):
        rev = reverse_number(i)
        pal = (i * 1000) + rev;
        if (primal.is_prime(pal)):
            continue
        factors = primal.prime_factors(pal)
        print("palindrome: ", pal, factors)
#        for j in factors:
#            if (j > 100 and j < 1000):
#                check = pal/j
#                if (check > 100 and check < 1000):
#                    print("found it! ", check)
#                    return check
        for j in reversed(factors):
            if (j < 1000):
                check = j
                mult = 1
                while (check >= 100 and check < 1000):
                    if (not pal % check):
                        other_check = int (pal / check)
                        if (other_check >= 100 and other_check < 1000):
                            print("found it!", check, ":", other_check)
                            return
                    mult = mult + 1
                    check = j * mult
