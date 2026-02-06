import sys

def check(r, c, val): # 숫자를 넣어도 되는지 검사하기
    # r:행, c:열, val: 값

    # 행 검사
    for r_num in board[r]:
        if r_num == val:
            return False

    # 세로 열 검사
    for i in range(9):
        if board[i][c] == val:
            return False

    # 3x3에서 시작 위치 점 찾기
    nr = (r//3)*3
    nc = (c//3)*3
    for i in range(nr, nr+3): # 시작점 nr 부터 nr+3까지 돌려야 nr~nr+3까지 검사
        for j in range(nc, nc+3): # nc~nc+3
            if board[i][j] == val:
                return False
    return True


def dfs(INDEX):
    if INDEX == len(zeros): # 0인 값을 다 채웠을 때를 검사. (재귀 종료)
        for row in board:
            print(*(row))
        exit(0)

    r, c = zeros[INDEX]
    for i in range(1, 10):
        if check(r, c, i):
            board[r][c] = i
            dfs(INDEX+1)
            board[r][c] = 0

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

zeros = []
for i in range(9): # 행과 열이 9*9
    for j in range(9):
        if board[i][j] == 0: # 0부분에 우리가 숫자를 넣어야함
            zeros.append((i, j))


dfs(0)