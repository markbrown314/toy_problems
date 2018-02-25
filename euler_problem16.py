# Power Digit Sum
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
# this is trivial in Python

value = 2**1000
val = str(value)
summ = 0
for i in range(0, len(val)):
    summ += int(val[i])

print("sum of digits:", summ)
