def solution(arr):
    x = 0
    while True:
        tmp = []
        for a in arr:
            if ((a >= 50) & (a%2==0)):
                tmp.append(a//2)
            elif ((a < 50) and (a%2!=0)):
                tmp.append(a*2 +1)
            else:
                tmp.append(a)
        if arr == tmp:
            return x
        else:
            x += 1
            arr = tmp