"""
Interface separeted

We created class Group and Teachers, and we can calculate average or maximumm value of marks or salaries.
So to create separate class for this calculation is better than put it in every class.

"""



class Group_info:
    def __init__(self):
        self.group = {
            'Anton':88,
            'Sergiy':75,
            'Masha':95
        }

class Teachers_info:
    def __init__(self):
        self.teachers ={
            'Anatoliy':1700,
            'Vitaliy':1800,
            'Pavel':2100
            }

class Avarege_max:
    def avarage(values):
        return str(round(sum(values)/len(values),2))
    def maximumm(values):
        return max(values)


a = Group_info()
b = Teachers_info()

c = Avarege_max

print(c.avarage(a.group.values()))
print(c.maximumm(b.teachers.values()))

