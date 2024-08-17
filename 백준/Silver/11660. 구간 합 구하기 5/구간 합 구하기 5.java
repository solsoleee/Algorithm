import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokens;
    private static StringBuilder output = new StringBuilder();
    private static int n,m;
    private static int[][] map;
    private static int[][] sum;

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());
        map = new int[n+1][n+1];
        sum = new int[n+1][n+1];

        for(int i=1; i<=n; i++){
            tokens = new StringTokenizer(input.readLine());
            for(int j=1; j<=n; j++){
                map[i][j] = Integer.parseInt(tokens.nextToken());
                sum[i][j] = map[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1];
            }
        }

        // m개의 줄 입력받기
        for(int i=0; i<m; i++){
            tokens = new StringTokenizer(input.readLine());
            int x1 = Integer.parseInt(tokens.nextToken());
            int y1 = Integer.parseInt(tokens.nextToken());
            int x2 = Integer.parseInt(tokens.nextToken());
            int y2 = Integer.parseInt(tokens.nextToken());

            // 누적합을 이용한 구간합 계산
            int res = sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1];
            output.append(res).append("\n");
        }
        System.out.print(output);
    }
}