T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input().split()
    answer = [0] * N
    
    d = (N+1)//2  
    i1, i2, i3 = 0, d, 0
    
    while i3 < N:
        if i1 < d:
            answer[i3] = card[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            answer[i3] = card[i2]
            i2 += 1
            i3 += 1
    print(f'#{tc}', *answer)