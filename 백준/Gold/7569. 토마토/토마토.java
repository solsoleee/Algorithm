import java.io.*;
import java.util.*;

public class Main {
    static boolean[][][] visited;
    static int deltas[][] = { {0,0,1},{0,1,0},{0,-1,0},{0,0,-1},{1,0,0},{-1,0,0} };
    static int box[][][];
    static int H,M,N;
    static Queue<int []> que;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken()); // 가로
        N = Integer.parseInt(st.nextToken()); // 세로
        H = Integer.parseInt(st.nextToken()); // 높이(상자 수)
        box = new int[H][N][M];
        visited = new boolean[H][N][M];
        que = new ArrayDeque<>();
        for(int h=0; h<H; h++) {
            for(int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                for(int j=0; j<M; j++) {
                    box[h][i][j] = Integer.parseInt(st.nextToken());
                    if(box[h][i][j] == 1) {
                        que.offer(new int[] {h, i, j, 0});
                        visited[h][i][j] = true;
                    }
                }
            }
        }
        int c = bfs();
        if(tomato()) System.out.println(c);
        else System.out.println(-1);
    }
    //다 익었는지 확인
    static boolean tomato() {
        for(int h=0; h<H; h++) {
            for(int i=0; i<N; i++) {
                for(int j=0; j<M; j++) {
                    if(box[h][i][j] == 0) return false; //익지 않았음
                }
            }
        }
        return true;
    }

    //익은 토마토
    static int bfs() {
        int res=0;
        while(!que.isEmpty()) {
            int temp[] = que.poll();
            int cnt = temp[3];
            res = cnt;
            for(int d[]: deltas) {
                int nz = temp[0]+d[0];
                int nx = temp[1]+d[1];
                int ny = temp[2]+d[2];
                if(check(nz,nx,ny) && !visited[nz][nx][ny] ) {
                    if(box[nz][nx][ny] == 0) {
                        que.offer(new int [] {nz,nx,ny,cnt+1});
                        visited[nz][nx][ny] = true;
                        box[nz][nx][ny] = 1; //익음
                    }
                }
            }
        }
        return res;
    }

    static boolean check(int z, int x, int y) {
        return (z>=0 && z<H && x>=0 && x<N && y>=0 && y<M);
    }
}
