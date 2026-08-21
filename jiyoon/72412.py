info = ["java backend junior pizza 150"]

query = ["java and backend and junior and pizza 100"]
d = "and"
for i in range(len(query)):
    query[i] = query[i].replace(" and ", " ").split()

for j in range(len(info)):
    info[j] = info[j].split()

result = [0]*len(query)

for i in range(len(query)):
    for j in range(len(info)):
        if ((query[i][0] == "-" or query[i][0] == info[j][0]) and
            (query[i][1] == "-" or query[i][1] == info[j][1]) and
            (query[i][2] == "-" or query[i][2] == info[j][2]) and
            (query[i][3] == "-" or query[i][3] == info[j][3])):

            if int(info[j][4]) >= int(query[i][4]):
                result[i] += 1
print(result)