def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        for n in str(num):
            if n == str(k):
                answer += 1
    return answer

# 리스트 컴프리헨션
def solution2(i, j, k):
    return sum([str(i).count(str(k)) for i in range(i, j+1)])