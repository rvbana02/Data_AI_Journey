marks=[67,89,33,67,94,78]
total=len(marks)
count=0
for m in marks:
     if(m>=33):
        count+=1

avg=sum(marks)/total

print("Total student:",total)
print("Passed student:",count)
print("Average marks:",avg)