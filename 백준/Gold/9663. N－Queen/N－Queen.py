n = int(input())
cols = [0] * n
count = 0

def can_place(row, col):
    for i in range(row):
        if cols[i] == col:
            return False

        if abs(row - i) == abs(col - cols[i]):
            return False

    return True

def solve(row):
    global count

    if row == n:
        count +=1
        return

    else:
        for col in range(n):
            if can_place(row, col):
                cols[row] = col
                solve(row+1)

solve(0)
print(count)