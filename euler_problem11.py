from grid import Grid
from functools import reduce

def solve():
    selections = []
    results = []
    selections.append([[0,0],[1,0],[2,0],[3,0]])
    selections.append([[0,0],[0,1],[0,2],[0,3]])
    selections.append([[0,0],[1,1],[2,2],[3,3]])
    selections.append([[0,0],[1,-1],[2,-2],[3,-3]])
    number_grid = Grid("problem11.txt", 20, 20)
    #number_grid.pretty_print()
    for x in range(0,20):
        for y in range(0,20):
            for selection in selections:
                results.append(reduce(lambda x,y: x*y, number_grid.select_items(selection, [x,y])))
    print(list(reversed(sorted(results))))
