import sys
cls = list(range(1,31))
for i in range(28):
    student = int(sys.stdin.readline())
    cls.remove(student)

print(cls[0])
print(cls[-1])