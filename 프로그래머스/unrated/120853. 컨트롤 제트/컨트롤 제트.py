def solution(s):
    ss = s.split()
    answer = 0
    for i in range(len(ss)):
        if ss[i] != 'Z':
            answer += int(ss[i])
        else :
            answer -= int(ss[i-1])
    return answer