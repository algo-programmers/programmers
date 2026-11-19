class Solution {
    int[]dr = {0,1,0,-1};
    int[]dc = {1,0,-1,0};
    public int[] solution(String[][] places) {
        int rooms =5;
        int[] answer = {};
        for(int roomNum = 0;roomNum<rooms;roomNum++){
            int res = checkPlace(room);
            answer[roomNum] = res;
        }
    }
    void checkPlace(room){
        int rows = 5, cols = 5;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                String str = room[i]
                if(room[i].charAt(j)=='P'){
                    boolean[][]visited = new boolean[rows][cols];
                    find(visited,i,j,1);
                }
            }
        }
    }
    boolean find(visited,i,j,depth){
        if(depth>2)return;
        visited[i][j] = true;
        for(int dir = 0;dir<4;dir++){
            int nr = i+dr[dir];
            int nc = j+dc[dir];
            if(!visited[nr][nc]){
                if(room[nr].charAt[nc]=='P') return false;
                if(room[nr].charAt[nc]=='O'){
                    boolean res = find(nr,nc);
                    if(!res) return false;
                }
            }

                for()
                    p있으면 answer[session++] = 0;
        }
    }
}

