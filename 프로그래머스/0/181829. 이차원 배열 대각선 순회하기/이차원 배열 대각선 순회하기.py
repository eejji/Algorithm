def solution(board, k):

    sum_li = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                sum_li.append(board[i][j])
                
    return sum(sum_li)