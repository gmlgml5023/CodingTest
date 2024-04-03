def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    return sorted(set(answer))

def solution2(numbers):
    return sorted({numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})