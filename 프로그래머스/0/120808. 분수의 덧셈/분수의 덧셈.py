def solution(numer1, denom1, numer2, denom2):
    lst = [numer1*denom2 + numer2 * denom1, denom1*denom2]

    na = [n for n in range(1, min(lst)+1) if (lst[0]%n==0) & (lst[1]%n==0)][-1]

    return [l//na for l in lst]