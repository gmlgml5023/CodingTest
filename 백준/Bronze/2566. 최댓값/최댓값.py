arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))
    
num_max = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if num_max <= arr[i][j]:
            num_max = arr[i][j]
            row = i+1
            col = j+1
            
print(num_max)
print(row, col)