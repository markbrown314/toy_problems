import os
from functools import reduce
from grid import Grid

os.chdir('C:/users/Mark Brown/desktop/Code/py')

with open("problem13.txt", 'r') as f:
    input_data = f.read()

numbers = [int (i) for i in input_data.splitlines()]

result = str(reduce(lambda x,y: x+y, numbers))
print(result)
print(result[0:10])

# method #2 manual method
grid = Grid("problem13.txt", 50, 100, 1)
grid.pretty_print()
selection = []
digits = []
add = 0
for i in range(0, 100):
    selection.append([0,i])

for x in range(50, 0, -1):
    add = reduce(lambda x,y: x+y, grid.select_items(selection, [x-1, 0])) + add
    digits.append(add % 10)
    add = int(add / 10)

rem = add
while add:
    digits.append(add % 10)
    add = int(add / 10)

print(list(reversed(digits))[:10])
