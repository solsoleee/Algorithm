import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder output = new StringBuilder();
    private static StringTokenizer tokens;
    private static int[][] map;
    private static boolean[] visited;
    private static int n;
    private static int[] startArr, linkArr;
    private static int min_diff = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());
        map = new int[n][n];
        visited = new boolean[n];


        for(int i=0; i<n; i++){
            tokens = new StringTokenizer(input.readLine());
            for(int j=0; j<n; j++){
                map[i][j] = Integer.parseInt(tokens.nextToken());
            }
        }
        // N/2개로 나누어서 조합만들기
        // EX) 1부터 n까지
        combi(0,0);
        System.out.print(min_diff);


    }
    private static void combi(int start, int cnt){
        if(cnt == n/2){
            startArr = new int[n/2];
            linkArr = new int[n/2];
            int size=0;
            int size2=0;
            for(int i=0; i<n; i++){
                if(visited[i]){
                    startArr[size++] = i;
                }
                else{
                    linkArr[size2++] = i;
                }
            }
            check();
            return;
        }
        for(int i=start; i<n; i++){
            if(!visited[i]){
                //스타트팀
                visited[i] = true;
                combi(i, cnt+1);
                visited[i] = false;
            }
        }
    }
    // 계산하는 함수
    private static void check() {
        //스타트팀
        int startScore=0;
        int linkScore=0;
        for (int i = 0; i < startArr.length - 1; i++) {
            for (int j = i+1; j < startArr.length; j++) {
                int row = startArr[i];
                int col = startArr[j];
                startScore += map[row][col];
                startScore += map[col][row];
                int row2 = linkArr[i];
                int col2 = linkArr[j];
                linkScore += map[row2][col2];
                linkScore += map[col2][row2];
            }
        }
        int res = Math.abs(linkScore-startScore);
        min_diff = Math.min(res, min_diff);
    }
}