import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer tokens;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static int n, b, c;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(input.readLine());  // 시험장의 개수
        int arr[] = new int[n];  // 각 시험장의 응시자 수
        tokens = new StringTokenizer(input.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(tokens.nextToken());
        }

        tokens = new StringTokenizer(input.readLine());
        b = Integer.parseInt(tokens.nextToken());  // 총감독관이 감시할 수 있는 인원 수
        c = Integer.parseInt(tokens.nextToken());  // 부감독관이 감시할 수 있는 인원 수

        long count = 0;  // 필요한 감독관 수의 최소값

        // 각 시험장에 대해 필요한 감독관 수 계산
        for (int i = 0; i < n; i++) {
            // 1. 총감독관 1명은 무조건 필요
            count++;

            // 2. 총감독관이 감시할 수 있는 인원을 제외한 나머지 계산
            int remaining = arr[i] - b;

            // 3. 부감독관이 필요한 경우 계산
            if (remaining > 0) {
                // 남은 인원을 부감독관이 감시할 수 있는 인원으로 나누기
                count += remaining / c;
                // 나머지가 있으면 부감독관 1명 더 필요
                if (remaining % c > 0) {
                    count++;
                }
            }
        }

        // 필요한 감독관 수 출력
        System.out.println(count);
    }
}