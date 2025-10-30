

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n, m;
	static int map[][];
	static int ans = Integer.MAX_VALUE;
	static boolean visited[][];
	static int[][] deltas = {{0, 0}, {1, 0}, {1, -1}, {1, 1}};
	static Queue<int[]> que;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		que = new ArrayDeque<>();
		visited = new boolean[n][m];
		map = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());

			}
		}
		for (int i = 0; i < m; i++) {
			que.offer(new int[] {0, i, 0, map[0][i]}); //출발지,방향, 현재수 첫 줄
			visited[0][i] = true;
		}
		//1,2,3중에 하나
		bfs();
		System.out.println(ans);
	}

	static boolean check(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}

	static void bfs() {
		while (!que.isEmpty()) {
			int t[] = que.poll();
			int direction = t[2];
			if (t[0] + 1 >= n) { //달에 도착
				ans = Math.min(ans, t[3]);
			}
			for (int j = 1; j < 4; j++) {
				if (direction == j)
					continue;
				int nx = t[0] + deltas[j][0];
				int ny = t[1] + deltas[j][1];
				if (check(nx, ny)) {
					que.offer(new int[] {nx, ny, j, t[3] + map[nx][ny]});
					//System.out.println(nx + " " + ny);
				}
			}
		}
	}
}
