class Solution {
    public int[] solution(int[] fees, String[] records) {
        int N = 10000;
        boolean[] isIn = new boolean[N]; // 현재 주차장에 있는지 여부
        boolean[] everIn = new boolean[N]; // 한 번이라도 입차했던 차량인지
        int cnt = 0; // 총 차량 수
        int[] answer;
        int[] inTime = new int[N]; // inTime[차량번호] = 마지막 입차시각 HHMM
        int[] timeAmounts = new int[N]; // timeAmounts[차량번호] = 누적 주차시간(분)

        for (int i = 0; i < records.length; i++) {
            String[] rec = records[i].split(" "); // {"12:34","5678","IN"}
            int plateNum = Integer.parseInt(rec[1]); // 차번호 5678
            String[] timeStr = rec[0].split(":"); // 시간 {"12","34"}
            int time = Integer.parseInt(timeStr[0]) * 100 + Integer.parseInt(timeStr[1]);

            if (rec[2].equals("IN")) {
                inTime[plateNum] = time;
                isIn[plateNum] = true;
                if (!everIn[plateNum]) {
                    everIn[plateNum] = true;
                    cnt++;
                }
            } else { // OUT
                timeAmounts[plateNum] += (time / 100) * 60 + time % 100
                        - (inTime[plateNum] / 100) * 60 - inTime[plateNum] % 100;
                isIn[plateNum] = false;
            }
        }

        // 출차 시간
        for (int i = 0; i < N; i++) {
            if (isIn[i]) {
                int endTime = 2359;
                timeAmounts[i] += (endTime / 100) * 60 + endTime % 100
                        - (inTime[i] / 100) * 60 - inTime[i] % 100;
            }
        }

        answer = new int[cnt];
        int idx = 0;
        for (int i = 0; i < N; i++) {
            if (everIn[i]) {
                answer[idx] = fees[1] + ((Math.max(timeAmounts[i] - fees[0], 0) + fees[2] - 1) / fees[2]) * fees[3];
                idx++;
            }
        }
        return answer;
    }
}