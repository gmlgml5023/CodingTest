def solution(a, b):
    num1 = f'{a}{b}'
    num2 = f'{b}{a}'
    return int(max(f'{b}{a}', f'{a}{b}'))