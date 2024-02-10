def solution(n, control):
    dic = {'w':1, 's':-1, 'd':10, 'a':-10}
    return n + sum([dic[c] for c in control])
