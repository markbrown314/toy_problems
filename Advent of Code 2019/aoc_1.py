def calculate_fuel(mass):
    fuel = mass//3-2
    if fuel<0: fuel = 0
    return fuel
input_file = open("aoc_1.txt")
total_fuel = 0
for line in input_file:
    total_fuel += calculate_fuel(int(line))
input_file.close()
print(total_fuel)


 