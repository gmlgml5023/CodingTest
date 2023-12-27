def solution(s):
    return ''.join(sorted([st for st in s if s.count(st)==1]))

# 중복 조회를 줄일 수 있는 방법
def solution2(s):
    return ''.join(sorted([st for st in s if s.count(st)==1]))