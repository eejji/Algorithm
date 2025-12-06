def solution(my_string, is_suffix):
    end = len(my_string)
    
    for i in range(len(my_string)) :
        pre = my_string[i:end]
        if pre == is_suffix :
            return 1
        
    return 0