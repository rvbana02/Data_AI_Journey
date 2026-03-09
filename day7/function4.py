def sumoflist(lists):
    sum=0
    for list in lists:
        sum+=list
    return sum


lists=[3,5,7]
sum=sumoflist(lists)
print(sum)