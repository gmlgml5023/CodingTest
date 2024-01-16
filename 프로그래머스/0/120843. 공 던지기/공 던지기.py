def solution(numbers, k):
    return [n for n in numbers*k][(k-1)*2]