
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            term1=str(a)+str(a)+str(a)
            term2=str(b)+str(b)+str(b)
            term3=str(c)+str(c)+str(c)
            check=str(b)+str(a)+str(a)+str(c)
            add=int(term1)+int(term2)+int(term3)
            if add == int(check):
                print("yes! a=",a,"b=",b,"c=",c)
