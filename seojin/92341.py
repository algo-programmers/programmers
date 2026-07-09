# 카카오 - 주차요금 계산 (구현)
from collections import defaultdict
import math 

def solution(fees, records):
    answer = []
    in_car = []
    cars_in = {}
    cars_time = defaultdict(int)
    for info in records:
        time, car, inout = info.split()
        h, m = time.split(":")
        m_time = int(h) * 60 + int(m)
        if inout == 'IN':
            in_car.append(car)
            cars_in[car]=m_time
        if inout == 'OUT':
            in_car.remove(car)
            tm = cars_in.pop(car)
            cars_time[car] += m_time - tm
    for left_car in in_car:
        tm = cars_in.pop(left_car)
        cars_time[left_car] += 23*60+59 - tm 
    
    for a, b in sorted(cars_time.items()):
        if b <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((b - fees[0])/fees[2]) * fees[3] )
    
    
    return answer