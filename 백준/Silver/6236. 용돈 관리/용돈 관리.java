import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int[] arr;
    static int n, m;

    public static void main(String[] args) throws IOException {
        StringTokenizer tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        m = Integer.parseInt(tokens.nextToken());
        arr = new int[n];
        
        int sum = 0;
        int start = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input.readLine());
            sum += arr[i];
            start = Math.max(start, arr[i]);
        }

        int end = sum;
        int ans = end;

        while (start <= end) {
            int mid = (start + end) / 2;
            int cnt = 1; // 인출 횟수
            int money = mid; // 현재 인출한 금액
            
            for (int i = 0; i < n; i++) {
                if (arr[i] > money) { // 남은 금액으로 하루 지출을 못 막으면 재인출
                    cnt++;
                    money = mid;
                }
                money -= arr[i];
            }

            // 정확히 M번만 인출하도록 K 값을 조정
            if (cnt > m) {
                start = mid + 1; // 인출 횟수가 많으면 K 값을 늘려야 함
            } else {
                end = mid - 1;
                ans = mid; // 현재의 mid가 최소 K일 가능성 있음
            }
        }
        
        System.out.println(ans);
    }
}