def solution(box, n):
    answer = 1
    for x in [b//n for b in box]:
        answer = x * answer
    return(answer)
