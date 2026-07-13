class Solution {
	public int solution(int x, int y, int n) {
		boolean[] visited = new boolean[y + 1];
		int[] qValue = new int[y + 1];
		int[] qCount = new int[y + 1];
		
		int h = 0;
		int t = 0;
		
		qValue[t] = x;
		qCount[t] = 0;
		visited[x] = true;
		t++;
		
		while (h < t) {
			int val = qValue[h];
			int cnt = qCount[h];
			h++;
			
			if (val == y) {
				return cnt;
			}
			
			int[] nexts = {val + n, val * 2, val * 3};
			for (int next : nexts) {
				if (next <= y && !visited[next]) {
					qValue[t] = next;
					qCount[t] = cnt + 1;
					visited[next] = true;
					t++;
				}
			}	
		}
		return -1;
	}
}