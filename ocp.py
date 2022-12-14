""""
Open - close 

We created data in one class, and than we need to sort it. But we don't sort the Parent's class, we made additional
class for sorting and there we create new sorted data 

"""

import random
from faker import Faker


class  Group:
    def __init__(self):
        self.group_info = []
        self.groups = ['A','B','C','D']

    def add_student(self,name_of_group,name_of_student,birthdate,city,phone):
        self.group_info.append([name_of_group,name_of_student,birthdate,city,phone])

    def remove_student(self,student_name):
        for i in self.group_info:
            if student_name in i:
                self.group_info.remove(i)
class Student(Group):
    def __init__(self):
        super().__init__()
        
    def show_student_info(self,student_name):
        for i in self.group_info:
            if student_name in i:
                return {i[1]:('Group: '+str(i[0]),i[2],i[3],i[4])}
    def show_all_students(self):
        all_students = dict()
        for i in self.group_info:
            all_students[i[1]] = ('Group: '+str(i[0]),i[2],i[3],i[4])
        return all_students
        
        

class Sort:

    @staticmethod
    def sort(object):
        if type(object) == list:
            sorted_object = sorted(object)
            return sorted_object
        elif type(object) == dict:
            sorted_object = {key: value for key,value in sorted(object.items())}
            return sorted_object

fake = Faker()
a = Student()
a.add_student(random.choice(a.groups),'Anton','20.04.1997','Dnipro','+3809999999')
a.add_student(random.choice(a.groups),'Vasya',str(fake.date_of_birth()),fake.city(),fake.phone_number())
a.add_student(random.choice(a.groups),'Petya',str(fake.date_of_birth()),fake.city(),fake.phone_number())
a.add_student(random.choice(a.groups),'Masha',str(fake.date_of_birth()),fake.city(),fake.phone_number())

b = Sort()
print(b.sort(a.show_all_students()))
print(b.sort(a.group_info))
