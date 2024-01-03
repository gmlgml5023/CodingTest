def solution(n):
    fac = 1
    for i in range(1, 10+1):
        fac *= i
        if fac <= n:
            answer = i
            pass
    return answer