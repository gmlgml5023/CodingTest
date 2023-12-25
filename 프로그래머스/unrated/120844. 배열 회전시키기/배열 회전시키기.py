def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers[len(numbers)-1])
        answer.extend(numbers[:len(numbers)-1])

    elif direction == 'left':
        answer.extend(numbers[1:])
        answer.append(numbers[0])
    return answer