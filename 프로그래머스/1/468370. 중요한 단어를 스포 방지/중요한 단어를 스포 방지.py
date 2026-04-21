def is_spoiler(w_start, w_end, s_ranges):
    for s_start, s_end in s_ranges:
        if w_start <= s_end and s_start <= w_end:
            return True
    return False

def solution(message, spoiler_ranges):

    word_info_list = []
    start = 0

    for i, char in enumerate(message):
        if char == " ":
            word = message[start:i]
            if word: # 그 다음에도 만약 공백일 경우 대비해서 True인지 한번 검사
                word_info_list.append({
                    "word":word,
                    "start":start,
                    "end":i-1})
            start = i + 1

    last_word = message[start:]
    if last_word:
        word_info_list.append({
            "word":last_word,
            "start":start,
            "end":len(message)-1
        })

    word_status = {}

    for item in word_info_list:
        word = item['word']
        current_is_spoil = is_spoiler(item['start'], item['end'], spoiler_ranges)

        if word not in word_status:
            word_status[word] = current_is_spoil
        else:
            word_status[word] = word_status[word] and current_is_spoil

    important_word_count = 0
    for word in word_status:
        if word_status[word] == True:
            important_word_count += 1
        
    return important_word_count