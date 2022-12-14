"""
Dependency inversion

We have class Persons with some info about person and we have class Sort_student_or_teacher, wich can get
every collection and sort it by teachers or students, and it not depends on our upper class. If we don't get data
wich relates to students or teachers, we get massage, no sudents or teachers there.

"""



class Persons:
    def __init__(self):
        self.persons = []
    
    def add_person(self,*args):
        self.persons.append(args)
    
    def get_persons(self):
        return self.persons


class Sort_student_or_teacher:
    def __init__(self):
        self.groups = ['A','B','C','D']
        self.subjects = ['mathematic','culture','chemistry']
        self.students= []
        self.teachers = []
        

    def sort_by_persons(self,args):
        for i in args:
            for y in self.groups:
                if y in i:
                   self.students.append(i)
        for i in args:
            for y in self.subjects:
                if y in i:
                   self.teachers.append(i)

    def show_students(self):
        if len(self.students) == 0:
            return 'No students in list'
        return self.students
    
    def show_teachers(self):
        if len(self.teachers) == 0:
            return 'No teachers in list'
        return self.teachers

    
a = Persons()
b = Sort_student_or_teacher()
a.add_person('Anton','B','20.04.1997')
a.add_person('Vasya','chemistry','12,10,1991')
b.sort_by_persons(a.get_persons())
print(b.show_students())
print(b.show_teachers())

                   
                    
