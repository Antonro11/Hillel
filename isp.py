"""
Interface separeted

"""


class Teacher:
    def __init__(self):
        self.teachers = dict()

    def add_teacher_info(self,name,city,birthdate,salary):
        self.teachers[name] = [city,birthdate,salary]

class Group(Teacher):
    def __init__(self):
        super().__init__()
    
    def show_teachers(self):
        teachers =[i for i in self.teachers]
        return teachers
    def show_cities(self):
        cities = [{i:y[0]} for i,y in self.teachers.items()]
        return cities
    def show_birthdates(self):
        birthdates = [{i:y[1]} for i,y in self.teachers.items()]
        return birthdates
    def show_saralies(self):
        salaries = [{i:y[2]} for i,y in self.teachers.items()]
        return salaries

"""
    We made many small functions opposite to one big 

"""
    
a = Group()
a.add_teacher_info('Vera','Dnipro','20.04.95','1600')
a.add_teacher_info('Petya','Kiev','19.5.91','1800')
print(a.show_birthdates())
print(a.show_cities())
print(a.show_saralies())
