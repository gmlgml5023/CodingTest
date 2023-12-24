def solution(cipher, code):
    return ''.join([c[1] for c in enumerate(cipher) if c[0] % code == code-1])