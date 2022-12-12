""""
Open - close 

"""

import random
from faker import Faker


class Info:
    def __init__(self):
            self.lst_groups = ['A','B','C','D']
            self.lst_subjects = ['mathematic','culture','chemistry','geography']
            

class Teacher(Info):
    def __init__(self):
        super().__init__()
        self.teachers = list()
    
    def add_teachers(self,name,name_subject):
        if name_subject in self.lst_subjects:
            self.teachers.append([name_subject+':',name])
        else:
            print('Subject name is not found')
    
    def show_teachers(self):
        teachers_str = ''
        for lst in self.teachers:
            for item in lst:
                teachers_str+= item +' '
            teachers_str+='\n'
        return teachers_str[:-1]

        
class Students(Info):
    def __init__(self):
        super().__init__()
        self.students = list()
    
    def add_students(self,name,name_group,mark):
        if name_group in self.lst_groups:
            self.students.append(['Group '+name_group+':',name+',','average mark:',mark])
        else:
            print('Group is not found')
    
    def show_students(self):
        students_str = ''
        for lst in self.students:
            for item in lst:
                students_str += str(item) + ' '
            students_str+='\n'
        
        return students_str[:-1]
        
class Group(Students,Teacher):
    def __init__(self):
        super().__init__()
    
    def rating_groups(self):
        rating_dict = dict()
        for i in self.students:
            if i[0] not in rating_dict:
                rating_dict[i[0]] = i[-1]
            else:
                rating_dict[i[0]] += i[-1]
        for key in rating_dict:
            if rating_dict.get(key)==max(rating_dict.values()):
                best_group = key + ' Is the best gpoup'
            elif rating_dict.get(key)==min(rating_dict.values()):
                worst_group = key + ' Is the worst gpoup'
            
        return best_group+'\n'+worst_group

    def best_worst_student(self):
        student_marks =[i[-1] for i in self.students]
        for i in self.students:
            if i[-1] == max(student_marks):
                best_student = 'Best Studend: '+i[1]+' has '+str(i[-1])+' average mark'
            elif i[-1] == min(student_marks):
                worst_student = 'Worst Studend: '+i[1]+' has '+str(i[-1])+' average mark'
        return best_student+'\n'+worst_student

    """            
       We are not changing our parent class Info, but we can extend it by using arguments from it in other classes,
       like Students, Group, other
    """    

name_surname_teacher = Faker()
name_surname_student = Faker()
a = Teacher()
b = Students()
c = Group()
a.add_teachers(name_surname_teacher.name(),random.choice(a.lst_subjects))
a.add_teachers(name_surname_teacher.name(),random.choice(a.lst_subjects))
a.add_teachers(name_surname_teacher.name(),random.choice(a.lst_subjects))
b.add_students(name_surname_student.name(),random.choice(a.lst_groups),random.randint(1,100))
b.add_students(name_surname_student.name(),random.choice(a.lst_groups),random.randint(1,100))
b.add_students(name_surname_student.name(),random.choice(a.lst_groups),random.randint(1,100))


for i in range(30):
    c.add_teachers(name_surname_teacher.name(),random.choice(a.lst_subjects))
    c.add_students(name_surname_student.name(),random.choice(a.lst_groups),random.randint(1,100))

print(a.show_teachers())
print(b.show_students())


print(c.show_teachers())
print(c.show_students())
print(c.best_worst_student())
print(c.rating_groups())
