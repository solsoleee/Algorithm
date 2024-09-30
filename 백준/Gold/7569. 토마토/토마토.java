import java.io.BufferedReader;
import java.io.IOException;
import java.io.*;
import java.util.*;

public class Main {
    private static StringBuilder output = new StringBuilder();
    private static StringTokenizer tokens;
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m,h,count;
    private static int box[][][];
    private static boolean visited[][][];
    private static int deltas[][] = {{1,0}, {-1,0},{0,1},{0,-1}};
    private static int height[] = {1,-1};
    private static Queue<int[]> que;
    public static void main(String[] args) throws IOException {
        que = new ArrayDeque<>();
        tokens = new StringTokenizer(input.readLine());
        m = Integer.parseInt(tokens.nextToken());
        n = Integer.parseInt(tokens.nextToken());
        h = Integer.parseInt(tokens.nextToken());
        box = new int[h][n][m];
        visited = new boolean[h][n][m];
        for(int k=0; k<h; k++) {
            for(int i=0; i<n; i++) {
                tokens = new StringTokenizer(input.readLine());
                for(int j=0; j<m; j++) {
                    box[k][i][j] = Integer.parseInt(tokens.nextToken());
                    if(box[k][i][j]==1) {
                        que.offer(new int[] {k, i,j,0}); //익은것은 넣어줌
                        visited[k][i][j] = true;
                    }
                }
            }
        }
        bfs(0);
        if(check()) System.out.println(count);
        else System.out.println(-1);

    }

    private static void bfs(int c) {
        while(!que.isEmpty()) {
            int t[] = que.poll();
            int z = t[0];
            int x = t[1];
            int y = t[2];
            int cnt = t[3];

            count= Math.max(count, cnt);
            //위, 뒤 일 때 익은 토마토

            for(int i=0; i<2; i++){
                int nz = z+height[i];
                if(nz >=0 && nz<h) {
                    if(!visited[nz][x][y] && box[nz][x][y]==0) {
                        visited[nz][x][y]=true;
                        box[nz][x][y]=1;
                        que.offer(new int [] {nz,x,y,cnt+1});
                    }
                }
            }
            //상하좌우 익은 토마토
            for(int d[]: deltas) {
                int nx = x + d[0];
                int ny = y + d[1];
                if(nx >=0 && nx < n && ny>=0  && ny < m) {
                    if(!visited[z][nx][ny] && box[z][nx][ny]==0) {
                        visited[z][nx][ny] = true;
                        box[z][nx][ny] = 1;
                        que.add(new int[]{z, nx, ny,cnt+1});
                    }
                }
            }
        }
    }

    private static boolean check() {
        for(int k=0; k<h; k++) {
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                    if(box[k][i][j]==0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}