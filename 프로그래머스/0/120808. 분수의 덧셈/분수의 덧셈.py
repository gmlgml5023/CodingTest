def solution(numer1, denom1, numer2, denom2):
    num = numer1*denom2 + numer2 * denom1
    den = denom1*denom2
    yaksu = [n for n in range(1, min(num,den)+1) if (num%n==0) & (den%n==0)][-1]
    return [num/yaksu, den/yaksu]