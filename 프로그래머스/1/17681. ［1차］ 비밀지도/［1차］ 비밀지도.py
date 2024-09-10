def solution(n, arr1, arr2):
    
    map1 = [bin(a1)[2:].zfill(n) for a1 in arr1]
    map2 = [bin(a2)[2:].zfill(n) for a2 in arr2]

    result = [[''] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                result[i][j] += ' '
            elif map1[i][j] == '1' or map2[i][j] == '1':
                result[i][j] += '#'

    return [''.join(r) for r in result]
