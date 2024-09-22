def solution(name, yearning, photo):
    score_dic = dict(zip(name, yearning))
    return [sum(score_dic.get(nm, 0) for nm in p) for p in photo]          