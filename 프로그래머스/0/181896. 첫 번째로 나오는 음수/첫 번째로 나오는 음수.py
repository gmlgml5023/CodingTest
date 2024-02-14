def solution(num_list):
    m = [n for n in num_list if n < 0]
    return -1 if len(m)==0 else num_list.index(m[0])