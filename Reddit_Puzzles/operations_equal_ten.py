"""
WIP needs re-design.
r/puzzles/comments/g7x82u/spent_a_lot_on_this_and_still_cant_solve_it/
Use all of the following operations and numbers to make an equation which
will be equal to 10. Numbers: 14,12,9,7,3 Operations: ÷, ÷, ×, -
"""
from itertools import permutations

n = ["14","12","9","7","3", "(", ")", "(", ")","/", "/", "*", "-"]

res = 0

perm = permutations(n, len(n))
for op in set(perm):
    code = "res =" + op 
    print(code)
    try:
        exec(code)
        # print(res)
        if res == 10:
            print("found solution")
            break
    except:
        print("invalid code", code)