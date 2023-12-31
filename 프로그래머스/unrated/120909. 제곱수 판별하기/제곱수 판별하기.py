def solution(n):
    answer = 0
    for num in range(1, n):
        if n == num**2:
            answer = 1
            break
        else:
            answer = 2
    return answer

# 다른 사람 풀이
def solution2(n):
    return 1 if (n ** 0.5) % 1 == 0 else 2