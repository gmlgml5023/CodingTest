N = int(input())

for test_case in range(1, N+1):
    s = input()
    for i in range(1, 11):
        if s[:i] == s[i:2*i]:
            break
    print(f'#{test_case} {i}')