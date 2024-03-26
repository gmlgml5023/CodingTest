def solution(s):
    s = [int(n) for n in s.split()]
    return ' '.join([str(min(s)), str(max(s))])