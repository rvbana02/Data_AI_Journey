class Student:
    def __init__(self,fullname):
        print("Adding new obeject....")
        self.name=fullname
    def welcome(self):
        print("Welcome student")



s1=Student("raj")
s1.welcome()
print(s1.name)


s2=Student("sikku")
print(s2.name)