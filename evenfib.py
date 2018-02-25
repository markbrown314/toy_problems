def fib():
    sum = 0
    fibv = 2
    fibp = 1
    temp = 0
    while (fibv <= 4000000):
        print(fibp)
        if (not fibv % 2):
            sum += fibv
        temp = fibp
        fibp = fibv
        fibv += temp
    print(fibp)
    print("sum: ", sum)
