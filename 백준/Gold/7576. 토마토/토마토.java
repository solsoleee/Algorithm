

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int[][] deltas = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
	static int n, m;
	static int grid[][];
	static boolean visited[][];
	static Queue<int[]> que = new ArrayDeque<>();
	static int ans = Integer.MIN_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		m = Integer.parseInt(st.nextToken());
		n = Integer.parseInt(st.nextToken());
		grid = new int[n][m];
		visited = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				grid[i][j] = Integer.parseInt(st.nextToken());
				if (grid[i][j] == 1) {
					que.offer(new int[] {i, j, 0});
					visited[i][j] = true;
				}
			}
		}
		bfs();
		if (tomato())
			System.out.println(ans);
		else
			System.out.println(-1);
	}

	static void bfs() {
		while (!que.isEmpty()) {
			int t[] = que.poll();
			ans = Math.max(ans, t[2]);
			for (int d[] : deltas) {
				int nx = t[0] + d[0];
				int ny = t[1] + d[1];
				if (check(nx, ny) && !visited[nx][ny]) {
					if (grid[nx][ny] == 0) {
						grid[nx][ny] = 1;
						visited[nx][ny] = true;
						que.offer(new int[] {nx, ny, t[2] + 1});
					}
				}
			}
		}
	}

	static boolean tomato() {
		//다 익었는지 체크
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (grid[i][j] == 0)
					return false; //익지 않음
			}
		}
		return true;
	}

	static boolean check(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}

}
