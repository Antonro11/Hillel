# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python

def consonant_count(text):
    non_conconants = ['a', 'e', 'i', 'o', 'u']
    all = [chr(i).lower() for i in range(65,91)]
    result = 0

    for i in text:
        if i.lower() in all and i.lower() not in non_conconants:
            result+=1

    return result

print(consonant_count('helLo world'))
