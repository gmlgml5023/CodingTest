def solution(n):
    trial = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n*3+1
        trial += 1
        
    if trial > 500: return -1

    return trial
