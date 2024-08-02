T = int(input())
for tc in range(1, T+1):
    sen = input()
    print(f'#{tc} {int(sen == sen[::-1])}')