def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except:
            return False
    return False