def solution(arr, divisor):
    # result = sorted([a for a in arr if a % divisor==0])
    # if len(result) == 0: return [-1]
    # else: return result 

    return sorted([n for n in arr if n%divisor == 0]) or [-1]