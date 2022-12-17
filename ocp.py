""""
Open - close 

We have our main class Person which we could update by the other classes, but we are not changing it.

"""
import random


class Person:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

    
class Student(Person):
    def __init__(self,name,last_name):
        super().__init__(name,last_name)
    
    def give_student_status(self):
        return {self.name+' '+self.last_name:'Student'}

class Teacher(Person):
    def __init__(self,name,last_name):
        super().__init__(name,last_name)
    
    def give_teacher_status(self):
        return {self.name+' '+self.last_name:'Teacher'}

class Group(Person):
    def __init__(self,name,last_name):
        super().__init__(name,last_name)
        self.group_lst = []

    def add_to_group(self):
        self.group_lst.append({self.name+' '+self.last_name:random.choice(['A','B','C','D'])})
        return self.group_lst

a = Student('Anton','Riabkov')
b = Group('Anton','Riabkov')
print(a.give_student_status())
print(b.add_to_group())
