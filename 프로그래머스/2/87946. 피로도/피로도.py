from itertools import permutations
def solution(k, dungeons):
    N = len(dungeons)
    max_cnt = 0
    for perm in permutations(range(N)):
        # [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        remain = k
        cnt = 0
        for i in perm:
            min_required, fatigue = dungeons[i]
            if remain >= min_required:
                remain -= fatigue
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)
    return max_cnt