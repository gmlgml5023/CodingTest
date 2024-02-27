def solution(s):
    p = 0
    y = 0
    for l in s.lower():
        if l == 'p':
            p += 1
        elif l == 'y':
            y += 1
    return True if p==y else False
        
            