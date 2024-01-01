def solution(numbers):
    lst = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i !=j:
              lst.append(numbers[i]*numbers[j])
    return max(lst)