# 번호 확인 내역 확인 IN이다 들어온 시간 확인 차량 번호에 맞는 OUT 확인
# 시간이 있으면 (출차시간 - 입차 시간), 없으면 (2359 - 입차시간)
# 기본 요금 + [(확인 시간 - (기본 시간))/10] *] (단위 요금)
# 마지막으로 요금 append 해서 새로운 리스트에 넣기


def solution(fees, records):
    result = []
    total = {}

    for i in range(len(records)):
        if records[i][11:13] == "IN":
            flag = False

            for j in range(i + 1, len(records)):
                if records[j][6:10] == records[i][6:10] and records[j][11:14] == "OUT":
                    park = int(records[i][0:2]) * 60 + int(records[i][3:5])
                    out = int(records[j][0:2]) * 60 + int(records[j][3:5])
                    check = out - park

                    car = records[i][6:10]
                    total[car] = total.get(car, 0) + check

                    flag = True
                    break

            if not flag:
                park = int(records[i][0:2]) * 60 + int(records[i][3:5])
                out = 23 * 60 + 59
                check = out - park

                car = records[i][6:10]
                total[car] = total.get(car, 0) + check

    for car in sorted(total.keys()):
        check = total[car]

        if check <= fees[0]:
            result.append(fees[1])
        else:
            pay = fees[1] + ((check - fees[0] + fees[2] - 1) // fees[2]) * fees[3]
            result.append(pay)

    return result


    