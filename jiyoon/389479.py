players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
m = 3
k = 5

time = []
answer = 0

for i in range(len(players)):
    check = (players[i] // m)
    print(check)

    if check == 0 :
        continue
    elif check > 0 :
        if (check - len(time)) > 0 :
            add_time = (check - len(time))
            answer += add_time

            if time :
                for j in range(len(time)):
                    time[j] = time[j] - 1

            for i in range(add_time):
                time.append(k)
            
