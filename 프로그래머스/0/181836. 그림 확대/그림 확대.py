def solution(picture, k):
    answer = []
    for p in picture:
        ele = ''
        for e in p:
            ele += e*k
        answer.extend([ele]*k)
    return answer

def solution2(picture, k):
    return [p.replace('.', '.'*k).replace('x', 'x'*k) for p in picture for _ in range(k)]