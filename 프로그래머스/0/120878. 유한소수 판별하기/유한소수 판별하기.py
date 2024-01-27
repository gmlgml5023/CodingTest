def solution(a,b):
    for i in range(min(a,b), 0, -1):
        if (a%i==0)&(b%i==0):
            a = a//i
            b = b//i
    for n in [2,5]:
        while not b % n:
            b //= n
    return 1 if b == 1 else 2
