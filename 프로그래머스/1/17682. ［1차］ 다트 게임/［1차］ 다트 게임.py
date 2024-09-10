def solution(dartResult):
    square = {'S': 1, 'D': 2, 'T': 3}
    score = []
    tmp = ''
    for i, dart in enumerate(dartResult):
        if dart.isdigit():
            tmp += dart
        elif dart.isalpha():
            score.append(int(tmp) ** square[dart])
            tmp = ''
        elif dart == '*':
            if len(score) == 1:
                score[-1] = score[-1] * 2
            elif len(score) >= 2:
                score[-2:] = [s*2 for s in score[-2:]]
        elif dart == '#':
            if score:
                score[-1] = -score[-1]
    return sum(score)