import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> q = new ArrayDeque<>();                 // [index, priority]
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder()); // 최대 우선순위

        for (int i = 0; i < priorities.length; i++) {
            q.offer(new int[]{i, priorities[i]});
            max.offer(priorities[i]);
        }

        int printed = 0;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int idx = cur[0];
            int pri = cur[1];

            // 현재 최고 우선순위와 비교
            if (pri < max.peek()) {
                // 아직 최고가 아니면 뒤로 보냄
                q.offer(cur);
            } else {
                // 인쇄
                printed++;
                max.poll(); // 해당 우선순위 하나 소진
                if (idx == location) return printed;
            }
        }
        return -1; // 이론상 도달 X
    }
}
