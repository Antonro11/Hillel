class frange:
    def __init__(self,*args,start=0,finish=0,step=1):
        self.args = args
        self.start = start
        self.finish = finish
        self.step = step
        self.count = self.start - self.step
        if len(self.args) == 1:
            self.finish = self.args[0]
        elif len(self.args) == 2:
            self.start = self.args[0]
            self.finish = self.args[1]
        elif len(self.args) == 3:
            self.start = self.args[0]
            self.finish = self.args[1]
            self.step = self.args[2]
            self.count = self.start - self.step
        else:
            return 'Error'

        
    def __iter__(self):        
        self.count =self.start - self.step
        return self
    
    def __next__(self):
            if self.count + self.step < self.finish and self.step > 0:
                self.count += self.step
                return self.count
            elif self.count + self.step > self.finish and self.step < 0:
                self.count += self.step
                return self.count
            else:
                raise StopIteration
               
        


  
        
        
        

print(list(frange(5, -5,-0.5)))
print(list(frange(10)))
print(list(frange(2,5,0.5)))
print(list(frange(100,0)))

