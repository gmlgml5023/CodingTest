def solution(a, b):
    for i in range(min(a,b), 0, -1):
        if (a%i==0)&(b%i==0):
            a = a//i
            b = b//i
        while True:
            if b%2!=0: break
            b = b//2
        while True:
            if b%5: break
            b = b//5
    return 1 if b==1 else 2