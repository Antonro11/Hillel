"""
Dependency inversion

"""

from abc import ABC, abstractmethod

class IsStudent(ABC):
    
    @abstractmethod
    def go_to_unuversity(self):
        pass
    @abstractmethod
    def get_marks(self):
        pass

class IsTeacher(ABC):

    @abstractmethod
    def go_to_unuversity(self):
        pass
    
    @abstractmethod
    def get_salary(self):
        pass

class Student(IsStudent):

    def go_to_unuversity(self):
        return 'Go to university'
    
    def get_marks(self):
        return 'I can get marks'

class Teacher(IsTeacher):

    def go_to_unuversity(self):
        return 'Go to university'
    
    def get_salary(self):
        return 'I can get salary'

a = Teacher()
b =Student()
print(a.get_salary())
print(b.go_to_unuversity())
                   

                   
                    
