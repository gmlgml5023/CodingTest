def solution(n):
    composite = []
    for num in range(4, n+1):
        if len([i for i in range(1, num+1) if num%i==0]) > 2:
            composite.append(num)
    return len(composite)

def solution2(n):
    answer = 0
    for i in range(4, n+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                answer += 1
                break
    return answer