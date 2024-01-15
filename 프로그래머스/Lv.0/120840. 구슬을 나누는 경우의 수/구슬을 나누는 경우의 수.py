def solution(balls, share):
    answer, div = 1, 1
    for b in range(balls, balls-share, -1):
        answer *= b
    for s in range(share, 0, -1):
        div *= s
    return answer // div