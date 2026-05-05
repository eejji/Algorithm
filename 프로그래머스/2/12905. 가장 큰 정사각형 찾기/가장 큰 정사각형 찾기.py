def solution(board):
    n = len(board)
    m = len(board[0])

    max_side = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                if i > 0 and j > 0:
                    board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1

                if board[i][j] > max_side:
                    max_side = board[i][j] 
                    
    return max_side ** 2