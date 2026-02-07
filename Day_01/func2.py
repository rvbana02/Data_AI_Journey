def fact(a):
        f=1
        while(a>0):
            f=f*a
            a-=1
        return f


num=int(input("enter the number"))
print("factorial is=>",fact(num))