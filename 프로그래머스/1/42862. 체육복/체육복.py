def solution(n, lost, reserve):

    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    _lost.sort()
    _reserve.sort()

    num = 0
    for r in _reserve:
        f = r-1
        b = r+1

        if f in _lost:
            _lost.remove(f)
            num+=1
        elif b in _lost:
            _lost.remove(b)
            num+=1

    return n - len(_lost)