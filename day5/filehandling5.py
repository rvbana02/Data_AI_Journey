with open("students.txt","r") as f:
    i=0
    for line in f:
        data=line.strip().split(",")
        i+=1
        name=data[0]
        marks=int(data[1])
        if marks>60:
            print(f"{name}  is pass")
    print(i)
