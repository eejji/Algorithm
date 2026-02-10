T = int(input())

for i in range(T):
    result = input()

    n = []
    s = ""
    
    for i in range(len(result)):
        if result[i] == "O":
            s+=result[i]
        else:
            n.append(s)
            s=""
        if i == len(result)-1:
            n.append(s)
    
    ss = 0
    for i in range(len(n)):
        if n[i]:
            for j in range(len(n[i])):
                ss+=j+1

    print(ss)