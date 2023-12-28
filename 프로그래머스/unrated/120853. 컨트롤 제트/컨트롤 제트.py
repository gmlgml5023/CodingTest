def solution(s):
    ss = s.split()
    answer = 0
    for i in range(len(ss)):
        if ss[i] != 'Z':
            answer += int(ss[i])
        else :
            answer -= int(ss[i-1])
    return answer

def solution2(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            stack.pop()
    return sum(stack)