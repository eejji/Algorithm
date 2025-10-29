def solution(num_list):
    
    multi = 1 # 모든 원소 값들의 곱 결과
    sum1 = 0 # 모든 원소 값들의 합 결과
    sum_r = 0 # 합의 제곱 결과
    for i in num_list:
        multi *= i # 모든 원소의 곱
        sum1 += i # 모든 원소의 합
    sum_r = sum1**2 # num_list 길이 만큼 제곱하는 것이 아니기 때문에 따로 제곱
        
    if multi < sum_r:
        return 1
    else: return 0