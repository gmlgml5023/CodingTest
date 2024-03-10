def solution(a, d, included):
    return sum([a+(d*i[0]) for i in enumerate(included) if i[1]==True])

def solution2(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a+d*i) * int(included[i])
    return answer