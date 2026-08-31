class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1;
        int right = 100_000;

        while (left < right) {
            int level = left + (right - left) / 2;
            if (inTime(diffs, times, limit, level)) {
                right = level;
            } else {
                left = level + 1;
            }
        }
        return left;
    }

    private boolean inTime(int[] diffs, int[] times, long limit, int level) {
        long totalTime = times[0];

        for (int i = 1; i < diffs.length; i++) {
            totalTime += Math.max(0, diffs[i] - level) * (times[i - 1] + (long)times[i]) + times[i];

            if (totalTime > limit) {
                return false;
            }
        }
        return true;
    }
}


// time_curr, time_prev
// diff, level
// 수준 이하면 time_curr
// 수준 초과면 수준차만큼 틀림, 1번 틀릴때마다 time_prev + time_curr
// (diff-level)*(time_prev + time_curr) + time_curr
// 다시 풀면 안틀림

// 입력 diffs, times, limit
// 100,000  50,000  10,000  3  25
// 5         6000    300    20  1

// lv=3
//
