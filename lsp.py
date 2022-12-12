"""
Liskov subtitution

"""
class Student:
    def __init__(self):
        self.student_marks=dict()
    
    def add_student_marks(self,name,*marks):
        marks_lst=[]
        for i in marks:
            marks_lst.append(i)
            if type(i) != int or i<1 or i>100:
                marks_lst.pop()
        self.student_marks[name] = marks_lst
    
    def show_student_marks(self):
        return self.student_marks


class Group(Student):
    def __init__(self):
        super().__init__()
    
        
    def show_student_rating(self,name):
        for i in self.student_marks:
            if name == i:
                average_mark = sum(self.student_marks[name])//len(self.student_marks[name])
                if 90<average_mark<=100:
                    return name+' '+str(average_mark)+': Exellent' 
                elif 80<average_mark<=90:
                    return name+' '+str(average_mark)+': Very good' 
                elif 70<average_mark<=80:
                    return name+' '+str(average_mark)+': Good' 
                elif 60<average_mark<=70:
                    return name+' '+str(average_mark)+': Normal' 
                elif 50<average_mark<=60:
                    return name+' '+str(average_mark)+': Need to improve'
                else:
                    return name+' '+str(average_mark)+': Bad'
        return 'Student is not found'

"""
   In the parent's class "Student" we need to have type(str) like a first argument,
   and integers in range(1,100) in the all others, so we need a check. If the argument is not valid, we removing it.

"""


a = Group()
a.add_student_marks('Vasya',20,30,199,50)
a.add_student_marks('Petya',20,45,78,92,14,'some text')
a.add_student_marks('Vera',25,86,3,89,68,25,99)
print(a.show_student_rating('Petya'))
