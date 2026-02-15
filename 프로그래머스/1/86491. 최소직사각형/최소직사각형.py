def solution(sizes):
    new = []
    for i in range(len(sizes)):
        a = sizes[i][0]
        b = sizes[i][1]

        if a > b:
            new.append([a, b])
        else:
            new.append([b, a])
            
    aa, bb = [], []
    for i in range(len(new)):
        aa.append(new[i][0])
        bb.append(new[i][1])
        
    return max(aa) * max(bb)