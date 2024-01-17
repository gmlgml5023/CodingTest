def solution(n):
    num = 4
    composite = []
    while num <= n:
        if len([i for i in range(1, num+1) if num%i==0]) > 2:
            composite.append(num)
        num+=1
    return len(composite)