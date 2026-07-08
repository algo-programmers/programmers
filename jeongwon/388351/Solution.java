class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int len = schedules.length;
        for(int i=0;i<len;i++){
            int cnt = 0;
            int timeLimit = ((schedules[i]+10)%100>=60) ? schedules[i]+50 : schedules[i]+10;
            for(int j=0;j<7;j++){
                if(((j+startday)%7>=1 && (j+startday)%7<=5) && timelogs[i][j]<=timeLimit){
                    cnt++;
                }
            }
            if(cnt==5)answer++;
        }
        return answer;
    }
}