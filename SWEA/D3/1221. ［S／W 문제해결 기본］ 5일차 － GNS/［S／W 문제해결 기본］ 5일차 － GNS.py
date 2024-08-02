T = int(input())

for tc in range(1, T + 1):
    input()
    strr = input().split()
    num_sys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_list = [num_sys.index(s) for s in strr]

    for i in range(len(num_list) - 1):
        min_idx = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_idx]:
                min_idx = j
        num_list[i], num_list[min_idx] = num_list[min_idx], num_list[i]

    result = [num_sys[n] for n in num_list]
    print(f'#{tc}')
    print(*result)