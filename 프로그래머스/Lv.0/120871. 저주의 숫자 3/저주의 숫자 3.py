def solution(n):
    num_3x = [num3x for num3x in range(1,201) if (num3x%3!=0)&('3' not in str(num3x))][:100]
    num_10 = [num for num in range(1,101)]
    return num_3x[num_10.index(n)]

def solution2(n):
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer