def solution(a, b):
    for i in range(min(a,b), 0, -1):
        if (a%i==0) & (b%i==0):
            print(i)
            a = a//i
            b = b//i
            print(a,b)
        while True:
            if b%2: break
            b = b//2
            print('!',b)
        while True:
            if b%5: break
            b = b//5
            print('?', b)
    return 1 if b==1 else 2