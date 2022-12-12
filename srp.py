""""
Single responsibility

"""
import random
from faker import Faker

class Student:
    def __init__(self):
        self.students = dict()
        pass
    
    def add_student(self,name,*info):                        
        if name not in self.students:
            self.students[name] = info
        else:
            return 'This name is already in list'
    
    def show_students(self):
        return self.students     
    
    def remove_student(self,name):
        for i in self.students:
            if i ==name:
                delete = i
                break
        del self.students[delete]

                                    # Methods execute only one task:  (add, remove, show) 

a = Student()

faker_info = Faker()
for i in range(10):
    a.add_student(faker_info.name(),faker_info.city(),faker_info.email(),faker_info.phone_number())
print(a.show_students())

for i in range(5):
    a.remove_student(random.choice([i for i in a.students]))

print()
print(a.show_students())
