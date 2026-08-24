# info = ["java backend junior pizza 150"]

# query = ["java and backend and junior and pizza 100"]
# d = "and"
# for i in range(len(query)):
#     query[i] = query[i].replace(" and ", " ").split()

# for j in range(len(info)):
#     info[j] = info[j].split()

# result = [0]*len(query)

# for i in range(len(query)):
#     for j in range(len(info)):
#         if ((query[i][0] == "-" or query[i][0] == info[j][0]) and
#             (query[i][1] == "-" or query[i][1] == info[j][1]) and
#             (query[i][2] == "-" or query[i][2] == info[j][2]) and
#             (query[i][3] == "-" or query[i][3] == info[j][3])):

#             if int(info[j][4]) >= int(query[i][4]):
#                 result[i] += 1
# print(result)

from collections import defaultdict
from bisect import bisect_left

def solution(info,query):
    # 조건별로 지원자 점수를 저장할 딕셔너리
    score_dict = defaultdict(list)

    for person in info:
        data = person.split()

        language = data[0]
        job = data[1]
        career = data[2]
        food = data[3]
        score = int(data[4])

        #지원자 한 명당 16개의 조건 생성
        for a in [language, "-"]:
            for b in [job, "-"]:
                for c in [career, "-"]:
                    for d in [food, "-"]:
                        key = a + " " + b + " " + c + " " + d
                        score_dict[key].append(score)

    # 2. 조건별 점수 목록 정렬
    for key in score_dict:
        score_dict[key].sort()

    result = []

    # 3. 각 문의 처리
    for q in query:
        # "and" 제거 후 공백 기준으로 분리

        data = q.replace(" and ", " ").split()

        key = (
            data[0] + " "
            + data[1] + " "
            + data[2] + " "
            + data[3]
        )

        target_score = int(data[4])

        score_list = score_dict[key]

        index = bisect_left(score_list, target_score)

        count = len(score_list) - index
        result.append(count)

    return result