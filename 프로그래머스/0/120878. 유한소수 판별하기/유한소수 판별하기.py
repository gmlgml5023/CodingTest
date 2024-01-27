def solution(a,b):
    for i in range(min(a,b), 0, -1):
        if (a%i==0)&(b%i==0):
            a = a//i
            b = b//i
        while b%2==0:
            b //= 2
        while b%5==0:
            b //= 5
    return 1 if b==1 else 2