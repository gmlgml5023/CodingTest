def solution(my_str, n):

    trial = 1
    answer = []
    if len(my_str) % n == 0:
        while trial <= len(my_str)//n:
            answer.append(my_str[(trial-1)*n:trial*n])
            trial += 1
    else:
        while trial <= len(my_str)//n:
            answer.append(my_str[(trial-1)*n:trial*n])
            trial += 1
        answer.append(my_str[-(len(my_str)%n):])

    return answer