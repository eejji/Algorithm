from math import factorial

def solution(n, k):
    
    # n까지 있을 때 1부터 만들어 질 수 있는 경우의 수를 세기

    basket = [x for x in range(1, n+1)]
    answer = []

    k -= 1

    for i in range(n):
        nn = factorial(n-1-i)
        idx = k // nn
        answer.append(basket.pop(idx))

        k = k % nn
    
    return answer


