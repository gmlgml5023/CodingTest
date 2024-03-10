def solution(a, d, included):
    return sum([a+(d*i[0]) for i in enumerate(included) if i[1]==True])