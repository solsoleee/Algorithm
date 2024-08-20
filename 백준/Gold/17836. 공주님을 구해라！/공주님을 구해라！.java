import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static int n, m, t;
    private static int[][] map;
    private static boolean[][] visited;
    private static int[][] deltas = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public static void main(String[] args) throws IOException {
        StringTokenizer tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());
        t = Integer.parseInt(tokens.nextToken());
        map = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            tokens = new StringTokenizer(input.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(tokens.nextToken());
            }
        }

        // 원래 경로에서 공주에게 도착하거나 검을 찾은 경우의 최소 시간을 각각 구함
        int result = bfs(0, 0);
        
        // 결과 출력
        if (result == Integer.MAX_VALUE) {
            System.out.print("Fail");
        } else {
            System.out.print(result);
        }
    }

    private static int bfs(int startX, int startY) {
        Queue<int[]> que = new LinkedList<>();
        que.offer(new int[]{startX, startY, 0});
        visited[startX][startY] = true;

        int result = Integer.MAX_VALUE;
        int gramTime = Integer.MAX_VALUE;

        while (!que.isEmpty()) {
            int[] temp = que.poll();
            int x = temp[0];
            int y = temp[1];
            int cnt = temp[2];

            // 제한 시간 초과 시 종료
            if (cnt > t) {
                continue;
            }

            // 공주에게 도착한 경우
            if (x == n - 1 && y == m - 1) {
                result = Math.min(result, cnt);
                continue;
            }

            // 상하좌우 탐색
            for (int[] d : deltas) {
                int nx = x + d[0];
                int ny = y + d[1];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    visited[nx][ny] = true;

                    if (map[nx][ny] == 0) {
                        que.offer(new int[]{nx, ny, cnt + 1});
                    } else if (map[nx][ny] == 2) {
                        // 검을 발견한 경우
                        gramTime = cnt + 1 + (n - 1 - nx) + (m - 1 - ny);
                    }
                }
            }
        }

        // 검을 통해 가는 경우와 원래 경로 중 더 짧은 것을 선택
        if (gramTime <= t) {
            result = Math.min(result, gramTime);
        }

        return result;
    }
}