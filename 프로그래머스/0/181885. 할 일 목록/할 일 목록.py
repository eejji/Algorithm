def solution(todo_list, finished):
    a = []
    for i in range(len(todo_list)):
        if finished[i]:
            pass
        else:
            a.append(todo_list[i])
            
    return a