N = int(input())
names = []
n = 0
total_names = []
for _ in range(N):
    chat = input()
    if chat == 'ENTER':
        n += len(set(names))
        names = []
    else:
        names.append(chat)

n += len(set(names))
print(n)