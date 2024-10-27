import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static StringTokenizer tokens;
    static int n,k,l,d;
    static int[][]map;
    static boolean visited[][];
    static Queue<int[]> que;
    static Queue<int[]> back;
    static Map<Integer, Character> direction;
    static int[][] deltas = {{0,1}, {1,0},{0,-1},{-1,0}}; //+1하면 오른쪽 회전
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());
        map = new int [n][n];
        visited = new boolean[n][n];
        k = Integer.parseInt(input.readLine());
        direction = new HashMap<>();
        for(int i=0; i<k; i++) {
            tokens = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(tokens.nextToken()) -1;
            int b = Integer.parseInt(tokens.nextToken()) -1;
            map[a][b] = 1; //사과가 있다는 뜻
        }
        l = Integer.parseInt(input.readLine());
        for(int i=0; i<l; i++) {
            tokens = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(tokens.nextToken());
            char b = tokens.nextToken().charAt(0);
            direction.put(a,b);
        }

        //뱀의 위치
        que = new ArrayDeque<>();
        back = new ArrayDeque<>();
        que.offer(new int[] {0,0}); //뱀의 머리만
        back.offer(new int[] {0,0}); //꼬리..
        visited[0][0] = true;
        int len = 1; //뱀의 길이
        int t = 0; //초

        while(true) {

            t++;
            int loca[] = que.poll();
            int x = loca[0]; //뱀의 머리
            int y = loca[1];

            //벽이나 자기 자신의 몸과 부딪이면 끝
            int nx = x + deltas[d][0];
            int ny = y + deltas[d][1];
            if(!check(nx,ny) || !bamCheck(nx,ny)) {
                break;
            }

            //사과가 있는 경우, 없는 경우
            if(map[nx][ny]==1) {
                len ++;
                map[nx][ny] =0; //사과없어짐
            }
            //사과없을 때
            else {
                visited[x][y] = false;
                back.poll();
            }
            visited[nx][ny] = true;
            back.offer(new int[] {nx,ny});
            que.offer(new int [] {nx,ny});
            //System.out.println(nx +" " + ny +" " +t);

            //초에 해당하는 게 있으면
            if (direction.containsKey(t)) {
                if(direction.get(t) == 'D') turn(d,'D' );
                else if(direction.get(t) == 'L') turn(d, 'L');
            }
        }
        System.out.println(t);

    }

    //que에 뱀의 몸통과 부딪히는지 확인하는 함수
    static boolean bamCheck(int x, int y) {

        for(int b[] : back) {
            if(b[0] == x && b[1] ==y) return false;
        }
        return true;
    }
    static boolean check(int x, int y) {
        return x>=0 && x<n && y>=0 && y<n;
    }
    static void turn(int di, char c) {
        if(c == 'D') d = (di+1)%4;
        else d = (di-1 +4)%4;
    }
}