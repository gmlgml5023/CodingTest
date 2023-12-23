def solution(my_string):
    num = [str(n) for n in range(1,10)]
    return sum([int(s) for s in my_string if s in num])

# 다른 사람 풀이
def solution2(my_string):
    return sum([int(s) for s in my_string if s.isdigit()]) # isnumeric()도 가능


def solution3(my_string):
    answer = 0
    for s in my_string:
        try : answer = answer + int(s)
        except : pass
    return answer