marks=[56,34,67,89,44,33]
count=0

for i in marks:
   if(i>=50):
     count+=1



print(f"passed student{count}")
print("Max ",max(marks))
print("Min ",min(marks))
print("Avrerage ",sum(marks)/len(marks))
