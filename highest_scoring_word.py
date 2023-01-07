# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272


def high(string):

    lst = string.split()
    result_dict = dict()

    for i in lst:
        for y in range(len(i)):
            if i not in result_dict:
                result_dict[i]=ord(i[y])-96
            else:
                result_dict[i]+=ord(i[y])-96

    for i,y in result_dict.items():
        if y == max(result_dict.values()):
            return i
