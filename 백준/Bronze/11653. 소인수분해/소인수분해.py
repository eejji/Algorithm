'''
- 정수 N이 주어졌을 때, 소인수 분해 프로그램
소인수 분해 -> 2, 3, 4 ... 계속 나눠서 안나눠질때까지 출력해야함
'''

num = int(input())

# 2부터 시작 
for i in range(2, num+1):
    if num % i == 0: # num숫자가 i숫자로 나눠졌으면 ?
        while num % i == 0: # num, i가 계속 나눠질때까지(참) 반복
            print(i) # 출력 
            num = num / i #몫을 취함 - num 변경

