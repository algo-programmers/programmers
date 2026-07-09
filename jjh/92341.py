from collections import defaultdict

def solution(fees, records):
    answer = []
    t, f, dt, df = fees
    users = defaultdict(int)
    users_in = defaultdict()
    
    for r in records:
        times = int(r[:2])*60 + int(r[3:5])
        user = int(r[6:10])
            
        if r[-2:] == 'IN':
            users[user] -= times
            users_in[user] = True
        else:
            users[user] += times
            users_in[user] = False
            
    for u, e in users_in.items():
        if e:
            users[u] += 23*60 + 59

    for u, p in sorted(users.items()):
        price = f

        if p > t:
            price += int((p-t)/dt)*df
            if (p-t)%dt:
                price += df
        answer.append(price)        
        
    return answer