import java.util.*;

class Solution {
    static char[] d;
    static boolean[] used;
    static HashSet<Integer> made;   // 중복 숫자 제거용

    public int solution(String numbers) {
        d = numbers.toCharArray();
        used = new boolean[d.length];
        made = new HashSet<>();

        dfs("");                    // 길이 0에서 시작, 길이 1~len까지 전부 만들기

        int ans = 0;
        for (int x : made) if (isPrime(x)) ans++;
        return ans;
    }

    static void dfs(String cur) {
        if (!cur.isEmpty()) {
            made.add(Integer.parseInt(cur));      // 앞의 0은 parseInt가 알아서 처리
        }
        if (cur.length() == d.length) return;

        for (int i = 0; i < d.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            dfs(cur + d[i]);                      // 현재 자리 하나 붙이기
            used[i] = false;
        }
    }

    static boolean isPrime(int n) {
        if (n < 2) return false;                  // 0, 1 제외
        int r = (int)Math.sqrt(n);
        for (int i = 2; i <= r; i++) if (n % i == 0) return false;
        return true;
    }
}
