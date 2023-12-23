def solution(my_string):
    answer = ''
    for s in my_string:
        if s.islower():
            answer += s.upper()
        else:
            answer += s.lower()
    return answer

# 한줄로
def solution2(my_string):
    return ''.join([s.lower() if s.isupper() else s.upper() for s in my_string])