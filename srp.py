""""
Single responsibility


We made separete classes for creating data, and saving it to file, we are not doing it in one class or in one method

"""
import random
from faker import Faker
import csv

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
class Save:
    @staticmethod
    def save_to_csv(object):
        with open('file.csv','w') as file:
            writer = csv.writer(file)
            if type(object)== list and type(object[0])==list:
                for i in object:
                    writer.writerow(i)
            elif type(object) == dict:
                fist_raw = [i for i in object]
                writer.writerow(fist_raw)
                for i in object.values():
                    writer.writerow(i)

    
    

fake = Faker()
a = Student()
a.add_student(random.choice(a.groups),'Anton','20.04.1997','Dnipro','+3809999999')
a.add_student(random.choice(a.groups),'Vasya',str(fake.date_of_birth()),fake.city(),fake.phone_number())
a.add_student(random.choice(a.groups),'Petya',str(fake.date_of_birth()),fake.city(),fake.phone_number())
a.add_student(random.choice(a.groups),'Masha',str(fake.date_of_birth()),fake.city(),fake.phone_number())
print(a.show_student_info('Vasya'))
b = Save()
b.save_to_csv(a.group_info)

