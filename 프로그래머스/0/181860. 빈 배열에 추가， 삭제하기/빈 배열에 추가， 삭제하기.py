def solution(arr, flag):
    X = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(arr[i]*2):
                X.append(arr[i])
        else:
            X = X[:-arr[i]]
    return X