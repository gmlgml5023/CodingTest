def solution(arr, n):
    if len(arr) % 2 != 0:
        return [a[1]+n if a[0]%2==0 else a[1] for a in enumerate(arr)]
    else:
        return [a[1]+n if a[0]%2!=0 else a[1] for a in enumerate(arr)]