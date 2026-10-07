class Solution{

    public int solution(int n, int[][] computers){
        boolean[] visited = new boolean[n];
        int cnt = 0;
        for(int c=0;c<n;c++){
            if(!visited[c]) {
                cnt++;
                dfs(computers, c, n, visited);
            }
        }
        return cnt;
    }

    void dfs(int[][]computers, int c, int n, boolean[] visited){
        visited[c]=true;
        for(int i=0;i<n;i++){
            if(!visited[i] && computers[c][i]==1){
                dfs(computers, i, n, visited);
            }
        }
    }
}