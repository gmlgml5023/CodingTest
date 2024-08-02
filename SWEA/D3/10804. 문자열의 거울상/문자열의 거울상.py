T = int(input())
mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
for tc in range(1, T+1):
    strr = list(input())
    for i in range(len(strr)):
        strr[i] = mirror[strr[i]]
    print(f'#{tc} {"".join(strr[::-1])}')
