def solution(a, b):
    if ((a%2 == 0)and(b%2 != 0)) or ((a%2 != 0)and(b%2 == 0)):
        answer = 2*(a+b)
    elif (a%2 != 0) & (b%2 != 0):
        answer = a**2 + b**2
    else:
        answer = abs(a-b)
    return answer