T = int(input())
for test_case in range(1, T+1):
    s = input()
    print(f'#{test_case} {int(s == s[::-1])}')