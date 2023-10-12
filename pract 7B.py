class employee():#Super class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

class childemployee1(employee):#child class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
class childemployee2(childemployee1):#child class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
emp1 = employee('Kavya',19,7000)
emp2 = childemployee1('Zoha',20,3000)
print(emp1.age)
print(emp2.age)
