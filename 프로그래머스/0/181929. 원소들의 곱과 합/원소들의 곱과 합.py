def solution(num_list):
    a = 1
    b = 0
    for n in num_list:
        a *= n
        b += n
    return 1 if a < b**2 else 0