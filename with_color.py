from colorama import Fore


class Colored:
    def __init__(self,color):
        self.color = color
        self.colors = {'red':Fore.RED,'green':Fore.GREEN,'blue':Fore.BLUE,
        'yellow':Fore.YELLOW,'cyan':Fore.CYAN}
    def __enter__(self):
        if self.color in self.colors:
            print(self.colors[self.color])
    def __exit__(self,type,value,traceback):
        print(Fore.RESET)
        
         

with Colored('yellow'):
    print('Some text for check')
    print('More text for check')
print('Some text for check')
