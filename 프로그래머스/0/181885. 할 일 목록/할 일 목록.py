def solution(todo_list, finished):
    answer = []
    for i, v in enumerate(finished):
        if v != True:
            answer.append(todo_list[i])
    return answer