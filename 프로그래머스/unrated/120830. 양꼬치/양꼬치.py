def solution(n, k):
    price = 12000*n + 2000*k
    discount = n//10 * 2000

    return price - discount