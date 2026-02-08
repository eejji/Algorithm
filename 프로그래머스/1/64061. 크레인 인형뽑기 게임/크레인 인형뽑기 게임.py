def solution(board, moves):
    basket = [0]
    cnt = 0

    def pickup(col):
        for i in range(len(board[0])):
            if board[i][col] > 0:
                N = board[i][col]
                board[i][col] = 0
                return board, N

    for i in range(len(moves)):
        res = pickup(moves[i]-1)
        if res:
            board, N = res
            if basket[-1] == N:
                basket.pop(-1)
                cnt+=2
            else:
                basket.append(N)
                
    return cnt