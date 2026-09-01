// 폭격 최대 50만
// 구간 0~1억

import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, (a, b) -> Integer.compare(a[1], b[1]));
        int intercepted = 0;
        int cnt = 0;
        for(int i=0;i<targets.length;i++){
            if(targets[i][0]>=intercepted){
                intercepted = targets[i][1];
                cnt++;
            }
        }
        return cnt;
    }
}