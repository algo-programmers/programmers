

def solution(s):
    s = s.split()


    max_num = int(s[0])
    min_num = int(s[0])

    for i in range(len(s)):
        max_num = max(max_num, int(s[i]))
        min_num = min(min_num, int(s[i]))

    answer = f"{min_num} {max_num}"
    return answer

s = "1 2 3 4"