def to_seconds(time_str):
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):

    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)


    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if cmd == "next":
            pos += 10
            if pos > video_len:
                pos = video_len
        elif cmd == "prev":
            pos -= 10
            if pos - 10 < 0:
                pos = 0
        if op_start <= pos <= op_end:
            pos = op_end

    min = pos // 60
    sec = pos % 60
    return f"{min:02d}:{sec:02d}"