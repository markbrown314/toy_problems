# Permutation Step : Have the function PermutationStep(num) take the num parameter 
# being passed and return the next number greater than num using the same digits. 
# For example: if num is 123 return 132, if it's 12453 return 12534. If a number 
# has no greater permutations, return -1 (ie. 999).
from permutation import permute

def set_to_string(set):
    string = ''
    for item in set:
        string+=str(item)
    return string

def permutation_step(num):
    perm = sorted([int(set_to_string(item)) for item in permute(str(num))])
    for i in perm:
        if i > num:
            return i
    return -1

print(permutation_step(123))
print(permutation_step(12453))
print(permutation_step(999))

    