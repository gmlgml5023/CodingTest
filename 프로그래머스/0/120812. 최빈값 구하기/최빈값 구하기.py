def solution(array):
    max_cnt, answer = 0, 0
    for a in set(array):
        cnt = array.count(a)
        if max_cnt < cnt:
            max_cnt = cnt
            answer = a
        elif max_cnt == cnt:
            answer = -1
    return answer