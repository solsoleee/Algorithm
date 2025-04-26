import java.util.*;

class Solution {
    static int n, m;
    static int[][] info;
    static int answer = Integer.MAX_VALUE;
    static int len;
    static boolean[][][] visited;

    public int solution(int[][] _info, int _n, int _m) {
        info = _info;
        n = _n;
        m = _m;
        len = info.length;
        // 흔적 최대값 60, 60 정도 (최대 흔적합 3 * 20)
        visited = new boolean[len + 1][n + m + 1][n + m + 1];
        
        dfs(0, 0, 0);
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

    static void dfs(int idx, int aSum, int bSum) {
        if (aSum >= n || bSum >= m)
            return;
        
        if (aSum >= answer)
            return;
        
        if (idx == len) {
            answer = Math.min(answer, aSum);
            return;
        }

        if (visited[idx][aSum][bSum])
            return;
        visited[idx][aSum][bSum] = true;

        // 현재 물건을 A 도둑이 가져감
        dfs(idx + 1, aSum + info[idx][0], bSum);

        // 현재 물건을 B 도둑이 가져감
        dfs(idx + 1, aSum, bSum + info[idx][1]);
    }
}
