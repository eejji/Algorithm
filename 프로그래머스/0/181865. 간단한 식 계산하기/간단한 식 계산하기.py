def solution(binomial):
    n1, ops, n2 = binomial.split()
    n1, n2 = int(n1), int(n2)
    if ops == '+':
        return n1 + n2
    elif ops == '-':
        return n1 - n2
    else:
        return n1 * n2