import java.util.*;
class Solution {
    static int [][] maps;
    static boolean[][] visited;
    static int answer;
    static int[][] deltas={{0,1},{1,0},{-1,0},{0,-1}};
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        answer = 0;
        maps = new int[101][101]; //2배로 늘림
        visited = new boolean[101][101];
        int n = rectangle.length;
        for(int i=0; i<n; i++) {
            int x1 = rectangle[i][0];
            int y1 = rectangle[i][1];
            int x2 = rectangle[i][2];
            int y2 = rectangle[i][3];
            draw(x1*2, y1*2, x2*2, y2*2);
        }
        //System.out.println(Arrays.deepToString(maps));
        bfs(characterX*2, characterY*2, itemX*2, itemY*2);
        return answer/2;
    }
    static void bfs(int x, int y, int targetX, int targetY) {
        Queue<int[]> que = new ArrayDeque<>();
        visited[x][y] = true;
        que.offer(new int[]{x, y, 1});
        while(!que.isEmpty()) {
            int t[] = que.poll();
            if(t[0] == targetX && t[1] == targetY ) {
                answer = t[2];
                
            }
            for(int d[]: deltas) {
                int nx = t[0] + d[0];
                int ny = t[1] + d[1];
                if(check(nx, ny) && !visited[nx][ny]) {
                    if(maps[nx][ny] == 2) {
                        visited[nx][ny] = true;
                        que.offer(new int[] {nx,ny,t[2] +1});
                    }
                }
            }
        }
    }
    
    static boolean check(int x, int y) {
        return x>=0 && x<101 && y>=0 && y<101;
    }
    
    static void draw(int x1, int y1, int x2, int y2) {
        for(int i=x1; i<=x2; i++) {
            for(int j=y1; j<=y2; j++) {
                if(maps[i][j] == 1) continue;
                maps[i][j] =1;
                if(i == x1 || i==x2 || j==y1 || j==y2) {
                    maps[i][j] = 2;
                }
            }
        }
    }
}