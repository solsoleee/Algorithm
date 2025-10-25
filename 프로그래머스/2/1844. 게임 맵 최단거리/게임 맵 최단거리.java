import java.util.*;

class Solution {
    static int[][] graph;
    static boolean visited[][];
    static int[][] deltas = {{0,1},{1,0},{-1,0},{0,-1}};
    static int n,m;
    static boolean flag;
    static int answer;
    public int solution(int[][] maps) {
        answer = 0;
        n = maps.length;
        m = maps[0].length;
        visited = new boolean[n][m];
        graph = maps;
        bfs(0,0);
        
        if (flag) return answer;
        else return -1;
    }

    static void bfs(int x, int y) {
        Queue<int[]> que = new ArrayDeque<>();
        que.offer(new int[] {x, y,1});
        visited[x][y] = true;
        while(!que.isEmpty()) {
            int t[] = que.poll();
            int tx = t[0];
            int ty = t[1];
            int cnt = t[2];
            if(tx == n-1 && ty == m-1) {
                answer = cnt;
                //System.out.println(Arrays.toString(t));
                flag = true;
            }
            for(int d[]:deltas) {
                int nx = tx+d[0];
                int ny = ty+d[1];
                if(check(nx, ny) && !visited[nx][ny]) {
                    if(graph[nx][ny]==1) {
                        visited[nx][ny] = true;
                        que.offer(new int[]{nx,ny,cnt+1});
                    }
                }
            }
        }
        
    }    

    static boolean check(int x, int y) {
        return x>=0 && x<n && y>=0 && y<m;
    }
    
}