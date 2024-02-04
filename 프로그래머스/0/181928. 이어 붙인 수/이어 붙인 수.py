def solution(num_list):
    a = int(''.join([str(n) for n in num_list if n%2==0]))
    b = int(''.join([str(n) for n in num_list if n%2!=0]))
    return a+b