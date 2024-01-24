def solution(quiz):
    answer = []
    for q in quiz:
        formula, ans = q.split(' = ')
        num1, sb, num2 = formula.split()

        if sb =='+':
            cal = int(num1) + int(num2)
        elif sb == '-':
            cal = int(num1) - int(num2)

        if cal == int(ans):
            answer.append('O')
        else:
            answer.append('X')
    return answer