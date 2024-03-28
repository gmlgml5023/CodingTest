def solution(picture, k):
    answer = []
    for p in picture:
        ele = ''
        for e in p:
            ele += e*k
        answer.extend([ele]*k)
    return answer