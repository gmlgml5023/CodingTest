def solution(arr, k):
    answer = []
    for a in arr:
        if (a not in answer)&(len(answer) != k):
            answer.append(a)       

    if len(answer) < k:
        answer.extend([-1]*(k-len(answer)))
        
    return answer