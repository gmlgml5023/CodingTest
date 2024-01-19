def solution(dots):
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])

def solution2(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]

    return (max(x) - min(x))*(max(y) - min(y))