def solution(a, b):
    num1 = f'{a}{b}'
    num2 = f'{b}{a}'
    return max(int(f'{b}{a}'), int(f'{a}{b}'))