import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer tokens;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int n;
    static double[] per;
    static boolean[][] visited;
    static int[][] deltas = {{0,1}, {0,-1}, {1,0}, {-1,0}}; // 동서남북
    static double ans;

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        per = new double[4];
        visited = new boolean[30][30];
        
        // 확률 입력 및 퍼센트 계산
        for (int i = 0; i < 4; i++) {
            per[i] = Integer.parseInt(tokens.nextToken()) * 0.01;
        }

        // 시작 위치 방문 설정
        visited[15][15] = true;
        dfs(0, 1.0, 15, 15); // 초기 위치에서 dfs 시작
        System.out.printf("%.10f", ans);
    }

    static void dfs(int cnt, double probability, int x, int y) {
        // n번 이동 완료 시 확률 추가
        if (cnt == n) {
            ans += probability;
            return;
        }

        // 4 방향으로 이동 시도
        for (int i = 0; i < 4; i++) {
            int nx = x + deltas[i][0];
            int ny = y + deltas[i][1];
            
            // 이미 방문한 위치 제외
            if (visited[nx][ny] || per[i] == 0) continue;
            
            visited[nx][ny] = true;
            dfs(cnt + 1, probability * per[i], nx, ny);
            visited[nx][ny] = false; // 탐색 후 방문 해제
        }
    }
}