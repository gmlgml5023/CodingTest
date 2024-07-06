T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A < B : print(f'#{test_case} <')
    elif A > B : print(f'#{test_case} >')
    else :  print(f'#{test_case} =')