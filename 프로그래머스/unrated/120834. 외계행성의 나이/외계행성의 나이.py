def solution(age):
    alpha = 'abcdefghij'
    return ''.join([alpha[int(a)] for a in str(age)])