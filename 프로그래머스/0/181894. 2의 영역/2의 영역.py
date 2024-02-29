def solution(arr):
    idx_2 = [i for i, a in enumerate(arr) if a == 2]
    if len(idx_2) >= 1:
        return arr[idx_2[0]:idx_2[-1]+1]
    else:
        return [-1]