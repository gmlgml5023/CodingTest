def solution(box, n):
    answer = 1
    for b in box:
        answer *= b//n
    return(answer)

# 다른 사람 풀이
def solution2(box, n):
    x, y, z = box
    return (x//n) * (y//n) * (z//n )
