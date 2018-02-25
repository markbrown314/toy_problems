total = 0
adder = 0

for i in range(0, 666):
    adder = (adder * 10) + 6
    total = total + adder
    print(i+1, ": ", total," + ",adder)
