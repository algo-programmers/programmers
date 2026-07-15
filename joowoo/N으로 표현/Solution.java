class Solution {
    int min = Integer.MAX_VALUE;
    int n;
    int target;
    
    public int solution(int N, int number) {
        n = N;
        target = number;
        
        dfs(0, 0);
        
        return min > 8 ? -1 : min;
    }
    public void dfs(int cnt, int val) {
        if (cnt > 8) return;
            
        if (val == target) {
            min = Math.min(min, cnt);
            return;
        }
            
        int nn = 0;
        for (int i = 1; i <= 8 - cnt; i++) {
            nn = nn * 10 + n;
                
            dfs(cnt + i, val + nn);
            dfs(cnt + i, val - nn);
            dfs(cnt + i, val * nn);
            dfs(cnt + i, val / nn);
        }
    }
}