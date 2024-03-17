def solution(arr):
    t = 1
    while t < len(arr) :
        t *= 2
    return arr + [0]*(t-len(arr))
    