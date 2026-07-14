import java.util.*;

class Solution {
	public int solution(int n, int k, int[] enemy) {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		long my = n;
		
		for (int i = 0; i < enemy.length; i++) {
			pq.offer(enemy[i]);
			
			if (pq.size() > k) {
				my -= pq.poll();
				
				if (my < 0) {
					return i;
				}
			}
		}
		return enemy.length;
	}
}
