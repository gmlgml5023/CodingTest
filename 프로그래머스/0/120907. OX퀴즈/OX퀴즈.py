def solution(quiz):
    answer = []
    for q in quiz:
        formula = q.split(' = ')[0]
        result = int(q.split(' = ')[1])

        num1 = int(formula.split()[0])
        sb = formula.split()[1]
        num2 = int(formula.split()[2])

        if sb =='+':
            cal = num1 + num2
        elif sb == '-':
            cal = num1 - num2

        if cal == result:
            answer.append('O')
        else:
            answer.append('X')
            
    return answer