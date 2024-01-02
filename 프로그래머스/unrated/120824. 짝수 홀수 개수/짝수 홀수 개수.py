def solution(num_list):
    r1 = len([n for n in num_list if n%2 == 0])
    r2 = len([n for n in num_list if n%2 == 1])

    return [r1, r2]
