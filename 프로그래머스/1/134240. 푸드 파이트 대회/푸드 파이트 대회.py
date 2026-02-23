def solution(food):
    new_food = food[1:]
    s = ""
    for i in range(len(new_food)):
        num = new_food[i]//2
        s+=str(i+1) * num

    s += "0"

    for i in range(len(new_food)-1, -1, -1):
        num=new_food[i]//2
        s+=str(i+1) * num
        
    return s