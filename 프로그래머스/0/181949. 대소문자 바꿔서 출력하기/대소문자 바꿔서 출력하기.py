str = input()

for i in range(len(str)):
    if str[i] == str[i].lower():
        print(str[i].upper(), end='')
    else:
        print(str[i].lower(), end='')
        

