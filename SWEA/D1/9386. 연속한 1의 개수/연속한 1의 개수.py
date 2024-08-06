T = int(input())
for tc in range(1, T+1):
    input()
    nums = input()
    split_num = nums.split('0')
    max_cnt = 0
    for sp in split_num:
        if max_cnt < len(sp):
            max_cnt = len(sp)
    print(f'#{tc} {max_cnt}')