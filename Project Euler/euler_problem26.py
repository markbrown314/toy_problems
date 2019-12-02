def unit_fraction(denominator):
    #print("1","/",denominator, ":", end = '')
    remainder_dict = {}
    count = 0
    dividend = 1
    while True:
        if denominator > dividend:
            dividend *= 10
        #print(dividend//denominator, end = '')
        dividend %= denominator
        if dividend == 0:
            break
        if dividend in remainder_dict:
            break
        remainder_dict[dividend]=True
        count += 1
    #print('')
    return count

count = 0
largest = 0

for i in range(1,1001):
    tcount = unit_fraction(i)
    if tcount > count:
        largest = i
        count = tcount
print("#", count, ":", largest)
