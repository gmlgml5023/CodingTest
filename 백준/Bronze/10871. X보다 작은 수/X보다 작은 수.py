x, y = map(int, input().split())
arr = map(int, input().split())

for a in arr:
    if a < y:
        print(a, end=' ')