'''file =open("data.txt","r")
data=file.read()
print(data)
file.close()'''
with open("data.txt","r")as file:
        data=file.read()
        print(data)


with open("data.txt","r")as file:
        data=file.readline()
        print(data)

with open("data.txt","r")as file:
        data=file.readlines()
        print(data)