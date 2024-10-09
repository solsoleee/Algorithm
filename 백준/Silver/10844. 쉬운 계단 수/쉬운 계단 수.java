import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        long[][] dp = new long[101][10];
        long mod = 1000000000;
        
        // 1자리 수일 때 1부터 9까지는 모두 계단 수
        for (int i = 1; i < 10; i++) {
            dp[1][i] = 1;
        }
        
        // 2자리 수부터 n자리 수까지 계산
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 10; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i - 1][j + 1] % mod;
                } else if (j == 9) {
                    dp[i][j] = dp[i - 1][j - 1] % mod;
                } else {
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod;
                }
            }
        }
        
        long result = 0;
        for (int i = 0; i < 10; i++) {
            result = (result + dp[n][i]) % mod;
        }
        
        System.out.println(result);
    }
}