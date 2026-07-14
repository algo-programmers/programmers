import heapq

def solution(n, k, enemy):

    attack = []
    total = 0
    
    for i in range(len(enemy)):
        
        total += enemy[i]
        
        heapq.heappush(attack, -enemy[i])
        
        if total > n :
            if k == 0 :
                return i
            
            largest_attack = -heapq.heappop(attack)
            total -= largest_attack
            k -= 1

    
    
    return len(enemy)