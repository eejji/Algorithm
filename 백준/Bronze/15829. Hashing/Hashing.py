n = int(input())
str = input()
mod = 1234567891
hash = 0

for i in range(n):
    cur = ord(str[i]) - 96
    hash += cur * 31 ** i
    
print(hash % mod)