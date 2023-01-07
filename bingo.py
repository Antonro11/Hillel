# https://www.codewars.com/kata/57f625992f4d53c24200070e

def bingo(ticket,win):

    mini_wins = 0

    for i in ticket:
        for y in i[0]:
            if ord(y) == i[1]:
                mini_wins +=1
    if mini_wins >=win:
        return 'Winner!'
    else:
        return 'Loser!'


print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1))
