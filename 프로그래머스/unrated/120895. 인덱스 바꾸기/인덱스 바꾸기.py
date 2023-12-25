def solution(my_string, num1, num2):
    string = [s for s in my_string]
    string[num1], string[num2] = string[num2], string[num1]
    return ''.join(string)