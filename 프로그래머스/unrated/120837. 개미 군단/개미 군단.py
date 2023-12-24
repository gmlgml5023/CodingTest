def solution(hp):
    return hp//5 + hp%5//3 + hp%5%3//1

# 다른 사람 풀이
def solution2(hp):
    answer = 0

    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer