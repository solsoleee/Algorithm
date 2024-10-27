import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, k, l, d;
    static int[][] map;
    static boolean[][] visited;
    static Deque<int[]> snake; // 뱀의 몸통과 머리 위치를 함께 관리
    static Map<Integer, Character> direction;
    static int[][] deltas = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // 방향 (우, 하, 좌, 상)
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];
        k = Integer.parseInt(input.readLine());
        direction = new HashMap<>();
        
        for (int i = 0; i < k; i++) {
            StringTokenizer tokens = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(tokens.nextToken()) - 1;
            int b = Integer.parseInt(tokens.nextToken()) - 1;
            map[a][b] = 1; // 사과 위치
        }
        
        l = Integer.parseInt(input.readLine());
        for (int i = 0; i < l; i++) {
            StringTokenizer tokens = new StringTokenizer(input.readLine());
            int a = Integer.parseInt(tokens.nextToken());
            char b = tokens.nextToken().charAt(0);
            direction.put(a, b);
        }

        // 뱀 초기화
        snake = new ArrayDeque<>();
        snake.offerFirst(new int[]{0, 0}); // 뱀의 머리 위치
        visited[0][0] = true;
        
        int t = 0; // 시간
        
        while (true) {
            t++;
            int[] head = snake.peekFirst(); // 현재 뱀의 머리 위치
            int nx = head[0] + deltas[d][0];
            int ny = head[1] + deltas[d][1];

            // 벽 또는 자기 자신과 충돌하면 게임 종료
            if (!check(nx, ny) || visited[nx][ny]) {
                break;
            }

            // 사과가 있는 경우, 없는 경우
            if (map[nx][ny] == 1) {
                map[nx][ny] = 0; // 사과 먹음
            } else {
                int[] tail = snake.pollLast(); // 꼬리 제거
                visited[tail[0]][tail[1]] = false;
            }

            // 뱀 머리를 새로운 위치에 추가하고 방문 처리
            snake.offerFirst(new int[]{nx, ny});
            visited[nx][ny] = true;

            // 방향 변경 확인
            if (direction.containsKey(t)) {
                if (direction.get(t) == 'D') {
                    d = (d + 1) % 4;
                } else if (direction.get(t) == 'L') {
                    d = (d + 3) % 4; // 왼쪽 회전
                }
            }
        }

        System.out.println(t);
    }

    static boolean check(int x, int y) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }
}