def solution(s):
    number_word = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    word_li = list(number_word.keys())
    
    ss = ""
    result = []
    
    for i in range(len(s)):
        if s[i].isdigit():
            result.append(s[i])
        else:
            ss+=s[i]
            if ss in word_li:
                result.append(str(number_word[ss]))
                ss = ""
                
    return int("".join(result))