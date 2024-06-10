nums = input().split()
print(sorted([n[::-1] for n in nums])[-1])