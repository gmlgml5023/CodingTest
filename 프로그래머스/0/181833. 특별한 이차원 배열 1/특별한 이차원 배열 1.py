def solution(n):
    lst1 = []
    for i in range(n):
        lst2 = []
        for j in range(n):
            if i == j: lst2.append(1)
            else: lst2.append(0)
        lst1.append(lst2)
    return lst1

def solution2(n):
    answer = [[0]*n for i in range(n)]
    for i in range(n): answer[i][i] = 1
    return answer