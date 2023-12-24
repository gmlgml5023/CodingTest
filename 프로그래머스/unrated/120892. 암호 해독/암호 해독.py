def solution(cipher, code):
    return ''.join([c[1] for c in enumerate(cipher) if c[0] % code == code-1])

# 다른 사람 풀이
def solution2(cipher, code):
    return cipher[code-1::code]