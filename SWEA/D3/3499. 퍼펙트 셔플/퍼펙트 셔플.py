'''
7
A B C D E F G
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()

    if N % 2 == 0:
        begin = arr[:N // 2]
        end = arr[N // 2:]

        lst = []
        for i in range(N // 2):
            lst.append(begin[i])
            lst.append(end[i])
    else:
        begin = arr[:N//2]
        end = arr[N//2+1:]

        lst = []
        for i in range(N // 2):
            lst.append(begin[i])
            lst.append(end[i])
        lst = lst + [arr[N//2]]
    print(f'#{tc}', *lst)