""""
Single responsibility

The methods of our classes is solving only problems related to the specific class.


"""

from colorama import Fore,Style

class  Group:
    def __init__(self):
        self.groups_students = dict()
    
    def add_group_sudent(self,group,student):
        if group in self.groups_students:
            self.add_group_sudent[group] +=[student]
        else:
            self.add_group_sudent[group] = [student]

class GoToUniversity:
    def __init__(self):
        pass

    def go_to_university(self):
        return 'Going to university'

    
class Student(GoToUniversity):
    def __init__(self):
        pass
    
    def get_mark(self):
        return 'Getting mark'

class Teacher(GoToUniversity):
    def __init__(self):
        pass
    
    def get_salary(self):
        return 'Getting salary'


class PrintColors:
    def __init__(self):
        pass

    def red_color(self,object):
        return Fore.RED + str(object) + Style.RESET_ALL

    def green_color(self,object):
        return Fore.RED + str(object) + Style.RESET_ALL
    
    

    

    
a = Student()
b = PrintColors()

print(a.get_mark())
print(b.red_color(a.go_to_university()))

