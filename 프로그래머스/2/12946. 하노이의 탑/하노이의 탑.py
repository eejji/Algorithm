def hanoi(n, F, E, T, a): # From 1번, Empty 2번, To 3번
    if n == 1:
        a.append([F, T])
        return

    else:
        hanoi(n-1, F, T, E, a)
        a.append([F, T])
        hanoi(n-1, E, F ,T, a)
        
def solution(n):
    a = []
    hanoi(n, 1, 2, 3, a)
    return a