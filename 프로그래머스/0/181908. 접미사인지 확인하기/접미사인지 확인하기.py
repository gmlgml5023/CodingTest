def solution(my_string, is_suffix):
    return 1 if my_string[-len(is_suffix):]==is_suffix else 0

def solution2(my_string, is_suffix):
    return int(is_suffix in [my_string[i:] for i in range(len(my_string))])