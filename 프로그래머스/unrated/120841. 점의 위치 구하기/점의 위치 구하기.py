def solution(dot):
    if (dot[0] > 0) & (dot[1] > 0) : return 1 
    if (dot[0] < 0) & (dot[1] > 0) : return 2
    if (dot[0] < 0) & (dot[1] < 0) : return 3
    if (dot[0] > 0) & (dot[1] < 0) : return 4

# 다른 사람의 풀이
def solution2(dot):
    quad = [(2,1), (3,4)]
    return quad[dot[0] < 0][dot[1] > 0]
