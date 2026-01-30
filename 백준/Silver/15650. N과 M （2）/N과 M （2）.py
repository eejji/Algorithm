N, M = map(int, input().split())
result = []  # 현재까지 선택한 숫자들

def backtrack(start):
    # start: 이번에 선택할 수 있는 시작 숫자
    
    # 종료 조건: M개를 다 선택했으면
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    # start부터 N까지 시도
    for i in range(start, N + 1):
        result.append(i)      # 선택
        backtrack(i + 1)      # 다음은 i+1부터
        result.pop()          # 선택 취소

backtrack(1)  # 1부터 시작