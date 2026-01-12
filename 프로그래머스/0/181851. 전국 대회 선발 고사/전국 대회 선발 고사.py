def solution(rank, attendance):
    at = sorted([rank[i] for i in range(len(rank)) if attendance[i]])[:3]
    a, b, c = rank.index(at[0]), rank.index(at[1]), rank.index(at[2])
    return 10000 * a + 100 * b + c