def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

def solution2(arr):
    return int(all(arr[i][j]==arr[j][i] for i in range(len(arr)) for j in range(len(arr[0]))))