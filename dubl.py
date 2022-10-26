def count_letter(string):
    list=[]
    dublicate=[]
    k=0
    for letter in string :
        if letter in list and letter not in dublicate:
            k+=1
            dublicate.append(letter)
        else:
            list.append(letter)
    return k


def dublicate(s):
    return len([ch for ch in (set(s.lower())) if s.lower().count(ch) > 1])

