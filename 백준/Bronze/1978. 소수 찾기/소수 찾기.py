def check(num):
    val = 1
    for i in range(2, num):
        if num % i == 0:
            val = 0
            break
    if num == 1:
        val = 0
        
    return val

N = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for n in num_list:
    cnt += check(n)
print(cnt)