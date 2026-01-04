def solution(myString, pat):
    a = myString.rfind(pat)
    
    return myString[:a+len(pat)]