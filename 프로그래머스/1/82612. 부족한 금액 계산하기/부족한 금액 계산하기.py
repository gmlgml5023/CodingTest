def solution(price, money, count):
    need = sum([p*price for p in range(1,count+1)])
    return need - money if need > money else 0