def solution(numbers, k):
    return [n for n in numbers*k][(k-1)*2]

def solution2(numbers, k):
    return numbers[2*(k-1) % len(numbers)]