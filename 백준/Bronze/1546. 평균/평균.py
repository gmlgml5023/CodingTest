n = int(input())
grade = list(map(int, input().split()))
grade = [g/max(grade)*100 for g in grade]
print(sum(grade)/n)