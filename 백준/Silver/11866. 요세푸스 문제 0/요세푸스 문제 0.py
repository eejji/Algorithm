import sys 

n,k = map(int, sys.stdin.readline().split()) 

queue = list(range(1,n+1))
index = 0
list = []

while len(queue) > 0:
    index += (k-1) 
    if index >= len(queue):
        index = index % len(queue)
    list.append(str(queue.pop(index)))

print("<", ", ".join(list), ">",sep="")