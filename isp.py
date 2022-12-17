"""
Interface separeted

We could make one class Group wich could make sorting our group dictionary by keys, or values.
But in this case we will need to write this functions again if we will need to use it on another dictionaryies.
It not goes to ISP.
So we separate this tho classes. 


"""


class Group:
    def __init__(self):
        pass

    def show_group(self):
        return {'Anton':85,'Zhenya':56,'Katya':97}

class SortDictValues:
    def __init__(self):
        pass
    
    def sort_dict(self,dict):
        sorted_dict = {key: value for key,value in sorted(dict.items(),key = lambda value:value[1])}
        return sorted_dict

class SortDictKeys:
    def __init__(self):
        pass
    
    def sort_dict(self,dict):
        sorted_dict = {key: value for key,value in sorted(dict.items())}
        return sorted_dict




a = Group()
b = SortDictValues()
print(b.sort_dict(a.show_group()))

