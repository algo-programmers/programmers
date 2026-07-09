class Solution {
    public int[] solution(int[] fees, String[] records) {
        int N = 10000;
        boolean[]isIn = new boolean[N]; // 들어온 차량
        int cnt = 0; // 총 차량 수
        int[]answer;
        int[][]inOutTime = new int[N][2]; // time[차량번호] = {입차시간, 출차시간}
        int[]timeAmounts; // timeAmounts[차량번호] = 주차시간(분)
        for(int i=0;i<N;i++){ time[i][1] = 2359;}
        for(int i=0;i<records.length;i++) {

            String[] rec = records[i].split(" "); // {"12:34","5678","IN"}

            int plateNum = Integer.parseInt(rec[1]); // 차번호 5678
            int inOutFlag = (rec[2].equals("IN")) ? 0 : 1; // 0=입차, 1=출차

            String[] timeStr = rec[0].split(":"); // 시간 {"12","34"}
            inOutTime[plateNum][inOutFlag] = Integer.parseInt(timeStr[0]) * 100 + Integer.parseInt(timeStr[1]);

            if (!isIn[plateNum]) {
                isIn[plateNum] = true;
                cnt++;
            }
        }
        timeAmounts = new int[cnt];
        int idx = 0;
        for(int i=0;i<N;i++) {
            if (isIn[i]) {
                timeAmounts[idx] = (inOutTime[i][1]/100)*60 + inOutTime[i][1]%100 - (inOutTime[i][0]/100)*60 - inOutTime[i][0]%100;
                answer[idx++] = fees[1] + ((Math.max(timeAmounts[idx] - fees[0], 0) + fees[2] - 1) / fees[2]) * fees[1];
            }
        }
        return answer;
    }
}