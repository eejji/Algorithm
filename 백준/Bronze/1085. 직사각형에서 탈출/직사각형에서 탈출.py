# 직사각형 탈출 
x,y,w,h = map(int, input().split())

print(min(x,y,(w-x),(h-y)))