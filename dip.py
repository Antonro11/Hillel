"""
Dependency inversion

"""

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

class Students(Info):
    def __init__(self):
        super().__init__()
        self.students = list()
    
    def add_students(self,name,name_group,mark):
        if name_group in self.lst_groups:
            self.students.append(['Group '+name_group+':',name+',','average mark:',mark])
        else:
            print('Group is not found')

class Result(Students,Teacher):
    def __init__(self):
        super().__init__()

    def print_result(self):
        return self.teachers,self.students

"""
Our parent class Info is not depend on our lower classes, but they are depends from it directly

"""

a = Result()
a.add_students('Vasya','B',65)
a.add_students('Petya','D',82)
a.add_teachers('Vadim','culture')
a.add_teachers('SVetlana','mathematic')
print(a.print_result())

