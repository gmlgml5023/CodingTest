def solution(array):
    answer = 0
    for a in array:
        answer += str(a).count('7')
    return answer


def solution2(array):
    return str(array).count('7')