import java.util.*;

class Solution {
    int n, m;
    int[][] land;
    int[][] comp;                 // 각 칸의 컴포넌트 id (0=없음)
    int[] compSize;               // id -> 크기
    static final int[][] DIR = {{1,0},{-1,0},{0,1},{0,-1}};

    public int solution(int[][] land) {
        this.land = land;
        n = land.length;
        m = land[0].length;
        comp = new int[n][m];
        compSize = new int[n * m + 1];   // 충분히 크게

        int id = 0;
        // 1) 전체를 한 번만 돌며 컴포넌트 라벨링 + 크기 계산
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1 && comp[i][j] == 0) {
                    compSize[++id] = bfsLabel(i, j, id);
                }
            }
        }

        // 2) 각 열에서 만나는 컴포넌트들의 크기를 합산(중복 제거)
        int answer = 0;
        for (int col = 0; col < m; col++) {
            int sum = 0;
            HashSet<Integer> seen = new HashSet<>();
            for (int row = 0; row < n; row++) {
                int cid = comp[row][col];
                if (cid != 0 && seen.add(cid)) {
                    sum += compSize[cid];
                }
            }
            answer = Math.max(answer, sum);
        }
        return answer;
    }

    // 시작점에서 같은 컴포넌트를 BFS로 라벨링하고 크기를 반환
    int bfsLabel(int sx, int sy, int id) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{sx, sy});
        comp[sx][sy] = id;
        int cnt = 1;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1];
            for (int[] d : DIR) {
                int nx = x + d[0], ny = y + d[1];
                if (in(nx, ny) && land[nx][ny] == 1 && comp[nx][ny] == 0) {
                    comp[nx][ny] = id;
                    cnt++;
                    q.offer(new int[]{nx, ny});
                }
            }
        }
        return cnt;
    }

    boolean in(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < m;
    }
}
