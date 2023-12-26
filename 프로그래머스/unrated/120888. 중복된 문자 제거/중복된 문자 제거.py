def solution(my_string):
    tmp = []
    for s in my_string:
        if s not in tmp:
            tmp.append(s)
    return ''.join(tmp)