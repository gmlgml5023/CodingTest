def solution(my_string, queries):
    my_string = list(my_string)   
    for q in queries:
        my_string[q[0]:q[1]+1] = my_string[q[0]:q[1]+1][::-1]
    return ''.join(my_string)
