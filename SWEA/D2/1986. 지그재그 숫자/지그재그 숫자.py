T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    ans = 0
    for n in range(1, num+1):
        if n % 2 != 0:
            ans += n
        else:
            ans -=n
    print(f'#{test_case} {ans}')
    
