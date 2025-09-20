A, B = map(int, input().split())
A_ = set(list(map(int, input().split())))
B_ = set(list(map(int, input().split())))

print(len(A_-B_) + len(B_-A_))