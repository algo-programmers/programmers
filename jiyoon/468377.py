def solution(cost, hint):
    n = len(cost)
    answer = float("inf")

    for mask in range(1 << (n-1)):
        hint_count = [0] * n
        total = 0

        for i in range(n-1):
            if mask & (1<<i):
                
                total += hint[i][0]

                for stage_number in hint[i][1:]:
                    hint_count[stage_number-1] += 1

        for i in range(n):
            usable_hint = min(hint_count[i], n - 1)
            total += cost[i][usable_hint]

        answer = min(answer, total)
    
    return answer