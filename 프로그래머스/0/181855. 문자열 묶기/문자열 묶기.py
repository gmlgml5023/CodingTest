def solution(strArr):
    lst = [0]*30
    for s in strArr:
        lst[len(s)-1] += 1
    return max(lst)