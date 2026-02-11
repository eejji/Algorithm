def solution(new_id):
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()

    # 2. 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 제외한 모든 문자 제거
    idd = ""
    for c in new_id:
        if "a" <= c and c <= "z":
            idd+=c
        elif c.isdigit():
            idd+=c
        elif c in ['-', '_', '.']:
            idd+=c

    # 3. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환 (정규식, While)
    while ".." in idd:
        idd = idd.replace("..", ".")

    # 4. 마침표가 처음이나 끝에 위치한다면 제거
    idd = idd.strip('.')

    # 5. 빈 문자열이라면 a를 대입
    if len(idd) == 0:
        idd+='a'

    # 6. 16자 이상이면 15문자까지// if ~
    if len(idd) >= 16:
        idd=idd[:15]
        
    if idd[-1] ==".":
        idd = idd[:-1]

    # 7. 2자 이하라면 마지막 문자 반복
    if len(idd)<=2:
        while len(idd) < 3:
            idd+=idd[-1]
            
    return idd