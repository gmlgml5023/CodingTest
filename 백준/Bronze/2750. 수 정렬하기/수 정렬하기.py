N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
for i in range(N):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(*arr, sep='\n')