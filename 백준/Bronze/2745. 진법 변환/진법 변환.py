N, B = input().split()
alphabet_list = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
num_list = list(range(36))

sum = 0
for i, n in enumerate(N):
    idx = alphabet_list.index(n)
    sum+=(num_list[idx]*(int(B)**(len(N)-1-i)))
        
print(sum)