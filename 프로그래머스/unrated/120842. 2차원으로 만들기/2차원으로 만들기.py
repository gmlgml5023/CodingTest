def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:i+n])
    return answer

# 리스트 컴프리헨션
def solution2(num_list, n):
    return [num_list[i:i+n] for i in range(0,len(num_list),n)]