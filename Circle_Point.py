class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def contains(self,point):
        if ((point.x-self.x)**2+(point.y-self.y)**2)**0.5 <=self.radius:
            return True
        else:
            return False
        

class Point:        
    def __init__(self,x,y):
        self.x=x
        self.y=y
        

circle = Circle(2,2,4)
point = Point(-1,1)
print(circle.contains(point))
