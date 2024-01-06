def solution(array, n):
    array.sort()
    tmp = [abs(a-n) for a in array]
    return array[tmp.index(min(tmp))]
    