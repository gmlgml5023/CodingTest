def solution(strArr):
    answer = []
    for a in strArr:
        if strArr.index(a) % 2 == 0:
            answer.append(a.lower())
        else:
            answer.append(a.upper())
    return answer