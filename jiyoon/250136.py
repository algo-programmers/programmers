def solution(land):
    answer = 0
    
    visited = [[0]*len(land[0]) for i in range(len(land))]
    oil_by_column = [0]* len(land[0])
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            
            if not visited[i][j] and land[i][j] == 1 :
                stack = [(i,j)]
                visited[i][j] = 1
        
                oil = 0
                occupied_columns = set()

                while stack:
                    ni,nj = stack.pop()
                    
                    oil += 1
                    occupied_columns.add(nj)
                    
                    for si,sj in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ki,kj = ni+si, sj+nj
                        
                        if 0 <= ki < len(land) and 0 <= kj < len(land[0]):
                            if not visited[ki][kj] and land[ki][kj] == 1:
                                stack.append((ki,kj))
                                visited[ki][kj] = 1
        
        
        
                for column in occupied_columns:
                    oil_by_column[column] += oil
                             

    return max(oil_by_column)




# len(land) 세로
# len(land[0]) 가로

