def collatz_seq(n):
    if not n%2:
        return int(n/2)
    return (3*n)+1

best = -1
best_n = -1

#for n in range(0, 1000000)
for n in range(1, 1000000):
    test = n
    i = 2
    while n != 1:
        n = collatz_seq(n)
        i += 1
    if i > best:
        best = i
        best_n = test
print("longest chain ", best, "n", best_n)
