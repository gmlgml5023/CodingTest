def solution(order):
    return len([n for n in str(order) if (int(n)%3==0) & (int(n)!=0)])