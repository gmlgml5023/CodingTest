def solution(my_string, is_prefix):
    return [my_string[:i+1] for i in range(len(my_string))].count(is_prefix)