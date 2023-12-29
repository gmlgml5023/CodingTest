def solution(my_string):
    s = my_string.split()
    answer = int(my_string.split()[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            answer += int(s[i+1])
        else:
            answer -= int(s[i+1])

    return answer

def solution2(my_string):
    return sum([int(i) for i in my_string.replace(' - ', ' + -').split(' + ')])