for tc in range(1, 11):

    N = int(input())
    ex = input()
    stack = []

    for i in range(N):
        if ex[i].isnumeric():
            stack.append(int(ex[i]))

        elif ex[i] == '+':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)

    print(f'#{tc} {stack[0]+stack[1]}')