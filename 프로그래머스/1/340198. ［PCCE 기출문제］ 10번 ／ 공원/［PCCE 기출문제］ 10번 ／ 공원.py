def solution(mats, park):
    ans = []

    right_max = len(park[0])
    down_max = len(park)

    def search_mat(s_x, s_y, mat):
        for y in range(s_y, s_y + mat):
            for x in range(s_x, s_x + mat):
                if park[y][x] != "-1":
                    return False
        return True

    for mat in mats:
        found = False
        for y in range(down_max - mat + 1):
            for x in range(right_max - mat + 1):
                if search_mat(x, y, mat):
                    ans.append(mat)
                    found = True
                    break
            if found:
                break

    if len(ans) > 0:
        return max(ans)
    else:
        return -1