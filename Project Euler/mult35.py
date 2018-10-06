def mult35(val):
    total = 0
    for i in range(0,val):
        if not i%3 or not i%5:
             #print("i ",i, "total ",total)
             total+=i
    print("total is ", total)
