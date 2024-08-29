T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    if N > M:
        A, B = B, A
        N, M = M, N
         
    lst = [sum(list(map(lambda x: x[0] * x[1], zip(B[i:i + N], A)))) for i in range(M-N+1)]
    print(f'#{tc} {max(lst)}')