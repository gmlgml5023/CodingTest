def solution2(arr, intervals):
    answer = []
    answer.extend(arr[intervals[0][0]:intervals[0][1]+1])
    answer.extend(arr[intervals[1][0]:intervals[1][1]+1])
    return answer

def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]