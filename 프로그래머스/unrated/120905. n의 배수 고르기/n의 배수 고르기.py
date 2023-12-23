def solution(n, numlist):
    return [num for num in numlist if num % n == 0]

# 다른 사람 풀이
def solution2(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
