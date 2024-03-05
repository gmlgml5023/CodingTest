def solution(numLog):
    answer = ''
    dic = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(1,len(numLog)):
        cha = numLog[i] - numLog[i-1]
        answer += dic[cha]
    return answer