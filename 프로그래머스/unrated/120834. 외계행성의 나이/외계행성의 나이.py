def solution(age):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([alpha[int(a)] for a in str(age)])