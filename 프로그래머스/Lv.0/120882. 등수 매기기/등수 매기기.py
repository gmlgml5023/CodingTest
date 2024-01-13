def solution(score):
    mean = [sum(s)/2 for s in score]
    return [sorted([sum(s)/2 for s in score], reverse=True).index(m)+1 for m in mean]