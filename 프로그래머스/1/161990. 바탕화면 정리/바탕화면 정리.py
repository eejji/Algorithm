def solution(wallpaper):

    left = len(wallpaper[0])
    right = 0

    for i in range(len(wallpaper)):
        row = wallpaper[i]
        for j in range(len(row)):
            if row[j] == "#":
                if j <= left:
                    left = j
                if j >= right:
                    right = j

    rows = []
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            rows.append(i)

    top = rows[0]
    bottom = rows[-1]

    return [top, left, bottom+1, right+1]