def solution(s):

    words = s.split(" ")
    result = []

    for word in words:
        result.append(word.capitalize())
    
    return " ".join(result)