
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int map[][];

	static boolean visited[][];
	static int n, m;
	static int count[][];
	static int deltas[][] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		count = new int[n][m];
		visited = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// map이 모두 0이 아닐때까지 반복
		int cnt = 0;
		boolean f = false;
		while (flag()) {
			//System.out.println(Arrays.deepToString(map));
			cnt++;
			melt(); // 빙하가 녹음
			excute(); // map에 반영
			//System.out.println(Arrays.deepToString(map));
			// 빙하가 나눠진 갯수
			if (glacier() >= 2) {
				f = true; // 두 덩이 이상으로 분리 될 때만
				break;
			}
		}
		if (f)
			System.out.println(cnt);
		else
			System.out.println(0);
	}

	static int glacier() { //빙하 개수
		int c = 0;
		visited = new boolean[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!visited[i][j] && map[i][j] > 0) {
					//bfs
					c++;
					bfs(i, j);
				}
			}
		}
		return c;
	}

	static void bfs(int x, int y) {
		Queue<int[]> que = new ArrayDeque<>();
		que.offer(new int[] {x, y});
		visited[x][y] = true;
		while (!que.isEmpty()) {
			int t[] = que.poll();
			for (int d[] : deltas) {
				int nx = t[0] + d[0];
				int ny = t[1] + d[1];
				if (check(nx, ny) && !visited[nx][ny]) {
					if (map[nx][ny] > 0) {
						//이어져 있음
						que.offer(new int[] {nx, ny});
						visited[nx][ny] = true;
					}
				}
			}
		}
	}

	static boolean flag() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] > 0) {
					return true;
				}
			}
		}
		return false; //모두다 0 이하
	}

	static boolean check(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}

	//빙하가 녹음
	static void excute() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] != 0) {
					if (map[i][j] - count[i][j] < 0) {
						map[i][j] = 0;
					} else
						map[i][j] -= count[i][j];
				}
			}
		}
	}

	//0이 아닌 빙하가 녹는 갯수
	static void melt() {
		count = new int[n][m];
		List<int[]> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] != 0) {
					list.add(new int[] {i, j}); //0이 아닌것들 넣고 count
				}
			}
		}
		//상하좌우 탐색해서 i,j,count에 넣기
		for (int i = 0; i < list.size(); i++) {
			int cnt = 0;
			int r = list.get(i)[0];
			int c = list.get(i)[1];
			// 상하좌우
			for (int d[] : deltas) {
				int nx = r + d[0];
				int ny = c + d[1];
				if (check(nx, ny) && map[nx][ny] == 0) {
					cnt++;
				}
			}
			count[r][c] = cnt;
		}
	}
}
