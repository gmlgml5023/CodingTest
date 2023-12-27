def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0

# 다른 사람 풀이
def solution2(before, after):
    return (sorted(before) == sorted(after))*1