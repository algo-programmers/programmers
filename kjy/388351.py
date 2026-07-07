def solution(schedules, timelogs, startday):
    answer = len(schedules)
    week = [startday]
    
    for i in range(6):
        if week[i]+1 < 8 :
            week.append((week[i]+1))
        else :
            week.append(1)
            
    test = 0
    
    while test < len(schedules):
        num = schedules[test] + 10
        
        if num % 100 >= 60 :
            num += 40
            
        for i in range(7):
            if week[i] != 6 and week[i] != 7:
                if timelogs[test][i] > num:
                    answer -= 1
                    break
        test += 1
    return answer
