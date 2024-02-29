def solution(q, r, code):
    # return ''.join([a for i, a in enumerate(code) if i % q == r])
    return code[r::q]