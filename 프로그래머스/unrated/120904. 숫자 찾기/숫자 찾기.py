def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).index(str(k)) + 1



def solution2(num, k):
    if str(k) in str(num):
        answer = str(num).index(str(k)) + 1
    else:
        answer = -1
    return answer