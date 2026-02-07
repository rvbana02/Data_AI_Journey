def fact(a):
    if(a==0):
        return 1
    return a*fact(a-1)



num=int(input("enter the number"))
print("factorial is:",fact(num))