def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                add = numbers[i] + numbers[j]
                if add not in answer:
                    answer.append(add)
    return sorted(answer)