def solution(array):
    answer = 0
    for a in array:
        for n in str(a):
            if n == '7':
                answer += 1
    return answer