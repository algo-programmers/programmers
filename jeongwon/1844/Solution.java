class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        int answer = -1;
        int[]dr = {0,1,0,-1};
        int[]dc = {1,0,-1,0};
        int[][]q = new int[n*m][3];
        int h = 0;
        int t = 1;
        q[0][0] = 0;
        q[0][1] = 0;
        q[0][2] = 0;
        while(h<t){
            int x = q[h][0];
            int y = q[h][1];
            int cnt = q[h][2];
            h++;
            if(x==n-1 && y==m-1){
                answer = cnt;
                break;
            }
            for(int i=0;i<4;i++){
                q[t][0] = x + dr[i];
                q[t][1] = y + dc[i];
                q[t][2] = cnt+1;
                t++;
            }
        }
        return answer;
    }
}