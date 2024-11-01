import java.util.*;
class Solution {
    
    static List<Integer> [] graph;
    static boolean visited[];
    static int min = Integer.MAX_VALUE;
    public int solution(int n, int[][] wires) {
        graph = new ArrayList [n+1];
        
        
        for(int i=0; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int w[]: wires) {
            graph[w[0]].add(w[1]);
            graph[w[1]].add(w[0]);
        }
        System.out.println(Arrays.toString(graph));
        for(int i=0; i<wires.length; i++) {
            visited = new boolean [n+1];
            graph[wires[i][1]].remove(Integer.valueOf(wires[i][0]));
            graph[wires[i][0]].remove(Integer.valueOf(wires[i][1]));
            //System.out.println(Arrays.toString(graph));
            
            int c = bfs(1);
            int d = n - c;
            //System.out.println(Math.abs(c-d));
            
            min = Math.min(min, Math.abs(c-d));
            
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
            
        }
        
        System.out.println(min);
        int answer = -1;
        return min;
    }
    static int bfs(int x) { //1번부터 연결되어 있는지 확인 몇개
        Queue <int[]> que = new ArrayDeque<>();
        que.offer(new int[] {x, 0});
        visited[x] = true;
        int res = 1;
        while(!que.isEmpty()) {
            int t[] = que.poll();
            int dx = t[0];
            int cnt = t[1];
            for(int next: graph[dx]) {
                if(!visited[next]) {
                    visited[next] = true;
                    que.offer(new int[] {next, cnt+1});
                    res++;
                }
            }
        }
        return res;
    }
    
}