n = int(input())
for _ in range(n):
    rep, letter = input().split()
    for l in letter:
        print(l*int(rep), end='')
    print()