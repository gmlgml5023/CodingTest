def solution(n, m):
    return [[i for i in range(1, m+1) if m%i==0 and n%i==0][-1], [j for j in range(1, n*m+1) if j%n==0 and j%m==0][0]]