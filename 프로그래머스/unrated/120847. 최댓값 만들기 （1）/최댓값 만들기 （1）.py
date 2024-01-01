def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]


# 다른 사람 풀이
# pop 활용

def solution2(numbers):
    num1 = 0
    num2 = 0
    answer = 0

    numbers.sort()

    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2

    return answer