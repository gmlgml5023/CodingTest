def solution(n):
    composite = []
    for num in range(4, n+1):
        if len([i for i in range(1, num+1) if num%i==0]) > 2:
            composite.append(num)
    return len(composite)