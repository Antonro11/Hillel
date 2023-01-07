#  https://www.codewars.com/kata/636173d79cf0de003d6834e4/train/python

def walk(path):

    lst = []
    if len(path) == 0:
        return 'Paused'

    for i in path:
        if i =='^':
            lst.append('up')
        elif i == 'v':
            lst.append('down')
        elif i == '>':
            lst.append('right')
        elif i == '<':
            lst.append('left')
    lst.append('to exept out_of_range_error') 

    count = 1
    result_str =''

    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            count+=1
        else:
            if count >1:
                result_str+=f'Take {count} steps {lst[i]}\n'
            else:
                result_str+=f'Take {count} step {lst[i]}\n'
            count = 1
    return result_str[:-1]
