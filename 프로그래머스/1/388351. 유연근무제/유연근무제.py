def time_h_m(time):

    hour = time // 100
    minute = time % 100
    return hour * 60 + minute

def solution(schedules, timelogs, startday):

    ans = 0
    for i in range(len(timelogs)):
        is_success = True
        limit_time = time_h_m(schedules[i]) + 10

        for j, timelog in enumerate(timelogs[i]):
            day = (startday + j - 1) % 7 + 1

            if day >= 6:
                continue

            if time_h_m(timelog) > limit_time:
                is_success = False
                break

        if is_success:
            ans += 1
            
    return ans