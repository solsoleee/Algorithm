import java.util.*;
class Solution {
    static int graph[][];
    static int len;
    static boolean visited[];
    public int solution(int n, int[][] computers) {
        int answer = 0;
        len = n;
        graph = new int[n][n];
        visited = new boolean[n];

        for(int i=0; i<len; i++) {
            if(!visited[i]) {
                //System.out.println(i);
                bfs(i, computers);
                answer++;
            }
            
        }
        return answer;
    }
    static void bfs(int x, int[][] computers) {
        
        Queue<Integer> que = new ArrayDeque<>();
        que.offer(x);
        visited[x] = true;
        while(!que.isEmpty()) {
            int temp = que.poll();
            for(int i=0; i<len; i++) {
                if(computers[temp][i] == 1 && !visited[i]) {
                    que.offer(i);
                     //System.out.println(i);
                    visited[i] = true;
                   
                }
            }
        }
    }
}