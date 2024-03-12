def solution(arr, queries):
    for i in range(len(queries)):
        for se in range(queries[i][0], queries[i][1]+1):
            arr[se] += 1
    return arr
