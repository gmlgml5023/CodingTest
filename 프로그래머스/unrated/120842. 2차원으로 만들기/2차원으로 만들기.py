def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        if i == 0:
            answer.append(num_list[0:n])
        else:
            answer.append(num_list[i:i+n])
    return answer