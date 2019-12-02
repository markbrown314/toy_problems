"""
🎅🏻 
--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to
other planets! To accurately calculate his position in space, safely align his warp drive,
and return to Earth in time to save Christmas, he needs you to bring him measurements from
fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the 
Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle
grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't
determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the
fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually
calculate the fuel needed for the mass of each module (your puzzle input), then add together
all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""
code_dict = {}

input_data="""
            1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,
            1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,
            13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,
            6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,
            2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,
            127,1,127,9,0,99,2,0,14,0
            """

for (i, code) in enumerate(input_data.split(",")):
    code_dict[i] = int(code)
code_dict[1] = 12
code_dict[2] = 2
pc = 0
res = 0
while True:
    op = code_dict[pc]

    if op == 99:
        break

    r1 = code_dict[pc+1]
    r2 = code_dict[pc+2]
    res = code_dict[pc+3]

    if op == 1:
        code_dict[res] = code_dict[r1] + code_dict[r2]
        pc += 4
        continue
    if op == 2:
        code_dict[res] = code_dict[r1] * code_dict[r2]
        pc += 4
        continue
    print("unknown op", op, "@", pc)
    exit(1)

print (code_dict[0])

