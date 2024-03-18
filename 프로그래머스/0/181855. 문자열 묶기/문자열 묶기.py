def solution(strArr):
    lst = [0]*31
    for s in strArr : lst[len(s)] += 1
    return max(lst)