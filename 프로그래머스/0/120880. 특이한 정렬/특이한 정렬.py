def solution(numlist, n):
    return sorted(numlist, key = lambda a : (abs(n-a), n-a))

def solution2(numlist, n):
    l = sorted([(abs(n-num), -num) for num in numlist])
    return [-m[1] for m in l]