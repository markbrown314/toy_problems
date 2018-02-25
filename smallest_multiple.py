import primal

def does_it_div(x, div_list):
    for i in div_list:
        if (x % i):
            return False
    return True

def eliminate_factors(x):
    num = list(range(1,x+1))
    pos = len(num)
    pos = int(pos / 2)
    for i in range(0, pos):
        if (not num[i]):
            continue
        #print("look num[",i,"]=", num[i])
        check = num[i]
        for j in range(pos, len(num)):
            #print("check ", check, " ? num[",j,"]=", num[j])
            if num[j]:
                if not num[j] % check:
                    #print("clear @ ", i)
                    num[i] = 0
                    break

    # crop list and sort
    num = sorted(list(filter(lambda l: l != 0, num)))
    print("dividers: ", num)
    mult = 0
    while True:
        mult += 1
        #print ("testing ", mult * num[0])
        if does_it_div(mult * num[0], num):
            print("found it:", mult * num[0])
            break
