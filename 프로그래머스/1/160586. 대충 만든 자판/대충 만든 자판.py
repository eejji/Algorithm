def solution(keymap, targets):
    min_press = {}

    for key in keymap:
        for i, char in enumerate(key):
            press_count = i + 1

            if char not in min_press:
                min_press[char] = press_count
            else:
                min_press[char] = min(min_press[char], press_count)

    total = []
    for target in targets:
        tt = 0
        for t in target:
            if t not in min_press:
                total.append(-1)
                break
            tt += min_press[t]
        else:
            total.append(tt)
    return total