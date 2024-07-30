def find_max(lst):
    max_idx = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_idx] : max_idx = i
    return max_idx

def find_min(lst):
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_idx] : min_idx = i
    return min_idx

for tc in range(1, 11):
    dump_count = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump_count):
        max_idx, min_idx = find_max(boxes), find_min(boxes)
        
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    result_max_idx, result_min_idx = find_max(boxes), find_min(boxes)

    print(f'#{tc} {boxes[result_max_idx]-boxes[result_min_idx]}')