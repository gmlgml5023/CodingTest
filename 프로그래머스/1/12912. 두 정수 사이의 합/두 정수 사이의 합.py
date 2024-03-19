def solution(a, b):
    return sum([n for n in range(a,b+1)]) if a<=b else sum([n for n in range(b,a+1)])