class Student:
    def __init__(self, n,i,g,b):
        self.name= n
        self.id= i
        self.gpa = g
        self.birthDate=b

    def gpaGood (self):
        return self.gpa >= 3.7
    
    def printInfo(self):
        print(self.name, self.id, self.gpa, self.gpaGood(),self.birthDate)
        
student1=Student("Jack",1877,3.4,"1988-01-02")#生成 student1 对象

student1.printInfo()

student1.name = "Big Jack"

print(student1.name,student1.gpaGood())#>>Big Jack False

student2= Student("Big Jack",1877,3.4,"1988-01-02")

print(student1 == student2)

student1.gender = "Female"

students=[student1,Student("Mary",1876,3.4,"1988-12-02"),
          Student("Tom",1782,3.8,"1988-11-02"),
          Student("Jane",1762,3.1,"1989-04-02")]

students.sort(key=lambda x:(-x.gpa,x.id))

for x in students:
    x.printInfo()
    
students.sort()

