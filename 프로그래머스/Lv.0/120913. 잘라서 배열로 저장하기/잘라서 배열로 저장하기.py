def solution(my_str, n):
    return [my_str[i : i+n] for i in range(0, len(my_str), n)]

def solution2(my_str, n):
    while my_str:
        if len(my_str) >= n:
            answer.append(my_str[:n])
            my_str = my_str[n:]
        else:
            answer.append(my_str)
            my_str=[]
    return answer