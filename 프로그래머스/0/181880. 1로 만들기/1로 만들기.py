def solution(num_list):
    cnt = 0
    for n in num_list:
        if n != 1:
            while n != 1:
                n = n//2
                cnt += 1
    return cnt