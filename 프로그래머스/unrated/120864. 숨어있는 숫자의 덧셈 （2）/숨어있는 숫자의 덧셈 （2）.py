def solution(my_string):
    for s in my_string:
        if s.isalpha():
            my_string = my_string.replace(s, ' ')

    lst = my_string.split()
    return sum([int(l) for l in lst])


def solution2(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())