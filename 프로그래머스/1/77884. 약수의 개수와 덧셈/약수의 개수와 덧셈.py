def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        lst = [i for i in range(1, n+1) if n%i==0]
        if len(lst) % 2 == 0:
            answer += n
        else: 
            answer -= n
    return answer