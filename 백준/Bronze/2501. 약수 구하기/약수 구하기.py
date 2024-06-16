n, k = map(int, input().split())
factors = [a for a in range(1, n+1) if n%a==0]

if len(factors) >= k:
    print(factors[k-1])
else:
    print(0)