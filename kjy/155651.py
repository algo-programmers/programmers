import heapq

def solution(book_time):
    def to_min(time):
        start = int(time[:2])
        end = int(time[3:])
        hour = start * 60 + end
        return hour
    
    times = []
    for start, end in book_time:
        start = to_min(start)
        end = to_min(end) + 10
        
        times.append([start,end])
    
    times.sort()
    
    rooms = []
    
    for start, end in times:
        if rooms and rooms[0] <= start :
            heapq.heappop(rooms)
        
        heapq.heappush(rooms, end)
        
    return len(rooms)

# 그리디
#시간을 분으로 바꾼다.
#시작 시간이 빠른 순으로 예약을 본다.
#각 방의 다음 사용 가능 시간을 저장한다.
#현재 예약이 가장 빨리 비는 방에 들어갈 수 있으면 재사용한다.
#못 들어가면 새 방을 만든다.
#마지막 방 개수가 답이다.
