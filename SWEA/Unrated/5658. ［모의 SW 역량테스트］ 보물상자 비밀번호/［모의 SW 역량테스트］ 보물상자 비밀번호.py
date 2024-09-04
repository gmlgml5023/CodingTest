T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()
    len_num = N//4
    lst = []
    for _ in range(N):
        num = num[-1] + num[:-1]
        for i in range(0, N, len_num):
            if num[i:i+len_num] not in lst:
                lst.append(num[i:i+len_num])
    answer = int(sorted(lst, reverse=True)[K-1], 16)
    print(f'#{tc} {answer}')