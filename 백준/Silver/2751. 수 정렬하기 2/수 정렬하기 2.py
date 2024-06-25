import sys

n = int(input())
num_list = set([int(sys.stdin.readline()) for _ in range(n)])
for num in sorted(list(num_list), reverse=True)[::-1]:
    print(num)
