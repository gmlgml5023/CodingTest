def solution(my_string):
    answer = int(my_string.split()[0])
    for i in range(1, len(my_string.split())-1, 2):
        if my_string.split()[i] == '+':
            answer += int(my_string.split()[i+1])
        else:
            answer -= int(my_string.split()[i+1])

    return answer