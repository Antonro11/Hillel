class Circle:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def contains(self,x_point,y_point):
        if (((x_point-self.x)**2+(y_point-self.y)**2)**0.5) <=self.radius:
            return True
        else:
            return False
