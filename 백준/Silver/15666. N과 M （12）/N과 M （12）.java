

import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] arr, res;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        res = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr);              // 정렬 필수 (비내림 + 중복 스킵 용)
        dfs(0, 0);                     // depth=0, start=0부터 시작
        System.out.print(sb.toString());
    }

    // 중복 조합: i를 start부터 돌리고, 다음 깊이도 i부터 (재사용 허용)
    static void dfs(int depth, int start) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(res[i]).append(' ');
            }
            sb.append('\n');
            return;
        }

        int last = -1; // 이 깊이에서 바로 전에 쓴 값 (중복 입력 방지용)
        for (int i = start; i < n; i++) {
            if (arr[i] == last) continue; // 같은 깊이에서 같은 숫자 재사용 금지
            res[depth] = arr[i];
            last = arr[i];
            dfs(depth + 1, i); // i 그대로 전달 → 같은 수 재사용 허용(중복 조합)
        }
    }
}
