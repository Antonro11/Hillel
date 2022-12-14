"""
Liskov Supstitution

We have same data in Students and Teachers: (name,city,phone) but we have data which is not same: (group),(salary).
So we created one class for (name,city,phone) and two more classas for (group) and (salary)
  

"""

import random
from faker import Faker
    
class PersonInfo:
    def __init__(self,name,city,phone):
        self.name = name
        self.phone = phone
        self.city = city
class Info_With_Group(PersonInfo):
    def __init__(self,name,city,phone,group):
        super().__init__(name,city,phone)
        self.group = group

class Info_with_subject(PersonInfo):
    def __init__(self,name,city,phone,subject):
        super().__init__(name,city,phone)
        self.subject = subject


    
    
class Student(Info_With_Group):
    def __init__(self, name, city, phone, group):
        super().__init__(name, city, phone, group)
    
    def show_student(self):
        return {self.name:(self.city,self.phone,self.group)} 

class Teacher(Info_with_subject):
    def __init__(self, name, city, phone, subject):
        super().__init__(name, city, phone, subject)
    
    def show_teacher(self):
        return {self.name:(self.city,self.phone,self.subject)} 
    
a = Student('Anton','Dnipro','+380999999','B')
b = Teacher('Vera','Kiev','+380777777','mathematic')
print(a.show_student())
print(b.show_teacher())
