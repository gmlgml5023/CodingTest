for tc in range(1, 11):
    input()
    password = list(map(int, input().split()))
    while password[-1] != 0:
        for i in range(1, 6):
            num = password.pop(0)-i
            if num <= 0:
                num = 0
            password.append(num)

            if password[-1] == 0:
                print(f'#{tc}', *password)
                break