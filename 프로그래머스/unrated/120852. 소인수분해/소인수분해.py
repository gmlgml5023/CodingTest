def solution(n):
    num = 2
    answer = []

    while num <= n:
        if n % num == 0:
            if num not in answer:
                answer.append(num)
            n //= num
        else:
            num += 1

    return answer