n = int(input())
arr = map(int, input().split())
v = int(input())

ans = 0
for a in arr:
    if a == v:
        ans += 1
print(ans)
        