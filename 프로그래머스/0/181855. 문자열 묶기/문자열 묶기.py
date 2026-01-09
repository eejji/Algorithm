from collections import Counter

def solution(strArr):
    lengths = [len(s) for s in strArr]
    count_dict = Counter(lengths)
    
    return max(count_dict.values())