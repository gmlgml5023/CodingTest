def solution(array, n):
    array.sort()
    tmp = []

    for a in array:
        tmp.append(abs(a-n))
    return array[tmp.index(min(tmp))]
    