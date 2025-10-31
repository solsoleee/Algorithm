import java.util.*;
class Solution {

    static boolean[][] visited;
    static int r,c;
    static int deltas[][] = {{1,0},{0,1},{-1,0},{0,-1}};
    static int grid[][];
    public int[] solution(int m, int n, int[][] picture) {
        r = m;
        c = n;
        grid = picture;
        int[] answer = new int[2];
        answer[0] = 0;
        answer[1] = 0;
        visited = new boolean[m][n];
        
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                if(!visited[i][j] && grid[i][j] !=0 ) {
                    int b = bfs(i,j);
                    visited[i][j] = true;
                    answer[0]++;
                    answer[1] = Math.max(b, answer[1]);
                }
            }
        }
        return answer;
    }
    //bfs 연결된 길이 구하기
    static int bfs(int x, int y) {
        Queue<int[]> que = new ArrayDeque<>();
        que.offer(new int[] {x, y});
        visited[x][y] = true;
        int cnt=1;
        while(!que.isEmpty()) {
            int t[] = que.poll();
            
            for(int d[]:deltas) {
                int nx = t[0] + d[0];
                int ny = t[1] + d[1];
                if(check(nx,ny) && !visited[nx][ny]) {
                    if(grid[x][y]==grid[nx][ny]) {
                        que.offer(new int[] {nx,ny});
                        visited[nx][ny] = true;
                        cnt++;
                    
                    }
                }
            }
        }
        return cnt;
    }
    
    
    static boolean check(int x, int y) {
        return x>=0 && x<r && y>=0 && y<c;
    }
}