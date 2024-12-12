import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer tokens;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int [][] map = new int[19][19]; // 오목판
    static int [] dx = {0, 1, -1, 1};
    static int [] dy = {1, 1, 1, 0};
    static boolean[][][] visited = new boolean[19][19][4];
    static Queue<int[]> deque = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        for (int i = 0; i < 19; i++) {
            tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < 19; j++) {
                map[i][j] = Integer.parseInt(tokens.nextToken());
                if (map[i][j] == 1 || map[i][j] == 2) {
                    deque.add(new int[] {i, j});
                }
            }
        }

        while (!deque.isEmpty()) {
            int[] t = deque.poll();
            int x = t[0];
            int y = t[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (!check(nx, ny)) continue;
                if (!visited[x][y][i] && countFive(x, y, i, map[x][y])) {
                    if(!check(x - dx[i], y - dy[i])) {
                        System.out.println(map[x][y]);
                        System.out.print((x + 1) + " " + (y + 1));
                        return;
                    }
                    if(check(x - dx[i], y - dy[i]) && map[x - dx[i]][y - dy[i]] != map[x][y]) {
                        System.out.println(map[x][y]);
                        System.out.print((x + 1) + " " + (y + 1));
                        return;
                    }
                }
            }
        }
        System.out.println(0); // 승부가 결정되지 않음
    }

    static boolean countFive(int x, int y, int dir, int color) {
        if (color == 0) return false; // 비었을 때
        int cnt = 1;
        visited[x][y][dir] = true;
        while (true) {
            x += dx[dir];
            y += dy[dir];
            if (!check(x, y) || map[x][y] != color) break;
            cnt++;
            visited[x][y][dir] = true;
        }
        return cnt == 5;
    }

    static boolean check(int x, int y) {
        return x >= 0 && x < 19 && y >= 0 && y < 19;
    }
}