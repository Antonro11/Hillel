"""

Liskov supstitution

We could make parentship between Teacher and FiredTeacher class, becouse they both can teach. 
But it not goes to LSP, becouse they have different status.
So we could make one Separate class Teach, or add fucntion could_teach in every class, it both will be right.


"""

class Person:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

class Student(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        return {self.name + ' ' + self.last_name:'Student'}

class Teacher(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
    
    def teacher(self):
        return {self.name + ' ' + self.last_name:'Teacher'}
    
    def could_teach(self):
        return 'Could teach'

class FiredTeacher(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
    
    def fired_teacher(self):
        return {self.name + ' ' + self.last_name:'Fired teacher'}

    def could_teach(self):
        return 'Could teach'

a =FiredTeacher('Evgeniy', 'Batkovich')
b = Teacher('Vasiliy','Petrovich')
print(a.fired_teacher())
print(b.teacher())

