def solution(arr, queries):    
    for i in range(len(queries)):
        for se in range(queries[i][0], queries[i][1]+1):
            arr[se] += 1
    return arr

def solution2(arr, queries):
    for s,e in queries:
        arr = [a+1 if s<=i<=e else a for i, a in enumerate(arr)]
    return arr
