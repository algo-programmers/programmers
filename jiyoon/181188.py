def solution(targets):
    targets.sort(key = lambda target: target[1])

    answer = 0
    last_end = -1

    for start, end in targets:
        if last_end <= start :
            answer +=1
            last_end = end

    return answer


# 문제를 단순화 하자!

# 1. 모든 구간을 통과하도록 최소 개수의 점을 찍는 문제
# 2. 한점으로 여러 구간을 처리하기 위해선 겹치는 곳을 찾아야 한다.
# 3. 가장 빨리 끝나는 구간부터 처리 = 그리디!