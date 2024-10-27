import java.util.*;

class Solution {
    static boolean visited[];
    static List<Integer> graph[];
    public int solution(int n, int[][] computers) {
        visited = new boolean[n+1];
        graph = new List[n+1];
        for(int i=0; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                if(computers[i][j] == 1) { //연결되어있다면
                    graph[i+1].add(j+1);
                }  
            }
        }
        int answer = 0;
        for(int i=1; i<=n; i++) {
            if(!visited[i]){
                bfs(i);
                answer++;
            }
        }
        //System.out.println(Arrays.toString(graph));
        
        //que로 몇개 연결 되었는지..

        
        return answer;
    }
    static void bfs(int x) {
        Queue<Integer> que = new ArrayDeque<>();
        que.offer(x);
        visited[x] = true;
        while(!que.isEmpty()) {
            int nx = que.poll();
            for(int next : graph[nx]) {
                if(!visited[next]) {
                    que.offer(next);
                    visited[next] = true;
                }
            }
        }
    }
}