def solution(num_list):
    a2 = 1

    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for n in num_list:
            a2 *= n
        return a2