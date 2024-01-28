def solution(num, total):
    s = ((num-1)*num)//2
    a = (total-s)//num
    return [n for n in range(a,a+num)]