# https://www.codewars.com/kata/57c15d314677bb2bd4000017/train/python

def doors(n):
    doors = ['close' for i in range(n)]

    step = 0

    for i in range(1,n+1):
        step = i
        while step<=n:
            if doors[step-1] =='open':
                doors[step-1] = 'close'
            else:
                doors[step-1] = 'open'
            step+=i
    return doors.count('open')
    
print(doors(10))
