def solution(code):
    mode = 0
    ret = ''
    
    for i, c in enumerate(code):
        if mode == 0:
            if c == '1':
                mode = 1
            elif i % 2 == 0:
                ret += c
        else:
            if c == '1':
                mode = 0
            elif i % 2 == 1:
                ret += c
                
    if len(ret) == 0:
        return "EMPTY"
    else:
        return ret