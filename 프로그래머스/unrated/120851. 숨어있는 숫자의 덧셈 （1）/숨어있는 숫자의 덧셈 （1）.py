def solution(my_string):
    num = [str(n) for n in range(1,10)]
    return sum([int(s) for s in my_string if s in num])