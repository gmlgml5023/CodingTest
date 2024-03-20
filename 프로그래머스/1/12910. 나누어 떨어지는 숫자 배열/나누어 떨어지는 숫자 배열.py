def solution(arr, divisor):
    result = sorted([a for a in arr if a % divisor==0])
    if len(result) == 0: return [-1]
    else: return result  