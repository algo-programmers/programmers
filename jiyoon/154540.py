def solution(maps):
    answer = []
    
    visited = [[0]*100 for i in range(100)]
    
    stack = []
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                stack.append((i,j))
                visited[i][j] = 1
                
                food = 0
                
                while stack:
                    ci, cj = stack.pop()
                    food += int(maps[ci][cj])
                    
                    for ni,nj in ((0,1),(1,0),(0,-1),(-1,0)):
                        xi,xj = ni+ci, cj+nj
                        
                        if 0 <= xi < len(maps) and 0 <= xj < len(maps[0]) and not visited[xi][xj] and maps[xi][xj] != "X" :
                            stack.append((xi,xj))
                            visited[xi][xj] = 1
                answer.append(food)
    
    answer.sort()
    
    if answer:
    
        return answer
    else :
        return [-1]