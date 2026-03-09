pass_c=0
fail_c=0

with open("marks.csv","r") as f:
    lines=f.readlines()
    for line in lines[1:]:
     data=line.strip().split(",")
     marks=int(data[1])
     if(marks>=60):
        pass_c+=1
        with open("pass.txt","a") as p:
            p.write(data[0])
            p.write(data[1])
            

     else:
        fail_c+=1

    print(f"pass student count is{pass_c}")
    print(f"fail student count is{fail_c}")
