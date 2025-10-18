import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        PriorityQueue <Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        Queue<int[]> que = new ArrayDeque<>();
        for(int i=0; i<priorities.length; i++) {
            que.offer(new int[]{i, priorities[i]});
            pq.offer(priorities[i]);
        }
        int rank = 1;
        while(!que.isEmpty()) {
            
            int temp[] = que.poll();
            //System.out.println(Arrays.toString(temp));
            if(temp[1]==pq.peek()) { // 같으면 poll
                pq.poll();
                if(temp[0] == location) return rank;
                rank++;
            }
            else{ 
                // 넣기
                que.offer(new int[]{temp[0], temp[1]});
            }
            
             
            
        }
        return rank;
    }
}