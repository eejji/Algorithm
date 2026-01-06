def solution(myString):
    a = myString.split('x')
    a2 = [i for i in a if i != '']
    
    return sorted(a2)