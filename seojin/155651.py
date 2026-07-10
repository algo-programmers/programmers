def solution(book_time):
    times = []
    need_rooms = []
    end_time = []
    answer = 0
    
    for enter, leave in book_time:
        hh, mm = enter.split(":")
        enter_time = int(hh)*60 + int(mm)
        HH, MM = leave.split(":")
        leave_time = int(HH)*60 + int(MM)
        times.append((enter_time, leave_time))
    times.sort(key = lambda x:x[0])
    end_time.append(times[0][1] + 10)
    for start, end in times[1:]:
        for i in range(len(end_time)):
            if end_time[i] <= start:
                end_time[i] = end + 10
                break
        else:
            end_time.append(end+10)
            
    answer = len(end_time)

    return answer