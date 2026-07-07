# 7월 7일 - 구현

def solution(schedules, timelogs, startday):
    answer = 0
    idx = 0
    for times in timelogs:
        max_time = schedules[idx] + 10
        # 958 + 10 => 1008 되어야하는데 968됨 -> 이 경우 고쳐주기 
        minute_time =  (max_time // 100) * 60 + (max_time % 100)
        hour_time = (minute_time // 60) * 100 + (minute_time % 60)
            
        for i in range(7):
            # startday = 5 -> date는 5,6,0,1,2,3,4 
            date = (startday + i) % 7
            if 1<= date <=5 :
                if times[i] > hour_time:
                    break
        else:
            answer += 1
        idx += 1
                
    return answer