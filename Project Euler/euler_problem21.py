from functools import reduce

def divisors(x):
    yield 1
    for i in range(2,x):
        if x%i == 0:
            yield i

res = 0

for num in range(1,10000):
    a = sum(divisors(num))
    b = sum(divisors(a))
    if a == b:
        continue
    if b == num:
        print (num, "loves", a)
        res += num

print(res)
