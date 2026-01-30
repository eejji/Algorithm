def solution(dartResult):
    dartResult = dartResult.replace('10', 'K')

    scores = []

    for char in dartResult:
        if char.isnumeric() or char == 'K':
            if char == 'K':
                scores.append(10)
            else:
                scores.append(int(char))

        elif char in ["S", "D", "T"]:
            if char == "S":
                scores.append(scores.pop(-1) ** 1)
            elif char == "D":
                scores.append(scores.pop(-1) ** 2)
            else:
                scores.append(scores.pop(-1) ** 3)

        elif char == "*":
            scores[-1] = scores[-1] * 2
            if len(scores) >= 2:
                scores[-2] = scores[-2] * 2

        elif char == "#":
            scores[-1] = scores[-1] * -1

    return sum(scores)