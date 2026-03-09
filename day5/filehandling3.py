with open("marks.csv", "r") as f:
    lines = f.readlines()

for line in lines[1:]:   # skip header
    data = line.strip().split(",")
    name = data[0]
    marks = int(data[1])
    
    if marks > 70:
        print(name, "Passed with good marks")
