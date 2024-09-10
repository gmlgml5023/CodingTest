def solution(dartResult):
    N = len(dartResult)
    square = {'S': 1, 'D': 2, 'T': 3}
    score = []
    tmp = ''
    for i in range(N):
        if dartResult[i].isdigit():
            tmp += dartResult[i]
        elif dartResult[i].isalpha():
            score.append(int(tmp) ** square[dartResult[i]])
            tmp = ''
        elif dartResult[i] == '*':
            if len(score) == 1:
                score[-1] = score[-1] * 2
            elif len(score) >= 2:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
        elif dartResult[i] == '#':
            if score:
                score[-1] = -score[-1]

    return sum(score)