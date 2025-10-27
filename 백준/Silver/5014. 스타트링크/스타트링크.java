

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int f, s, g, u, d;
	static int max_val = 1000000;
	static boolean flag;
	static int ans;
	static boolean visited[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		f = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		g = Integer.parseInt(st.nextToken()); //목표
		u = Integer.parseInt(st.nextToken());
		d = Integer.parseInt(st.nextToken());
		visited = new boolean[f + 1];

		bfs();
		if (flag)
			System.out.println(ans);
		else
			System.out.println("use the stairs");
	}

	//bfs
	static void bfs() {
		Queue<int[]> que = new ArrayDeque<>();
		que.offer(new int[] {s, 0});
		visited[s] = true;
		while (!que.isEmpty()) {
			int t[] = que.poll();
			int current = t[0];
			int cnt = t[1];
			if (current == g) {
				ans = cnt;
				flag = true;
				return;
			}
			if (current + u <= f && !visited[current + u]) {
				que.offer(new int[] {current + u, cnt + 1});
				visited[current + u] = true;
			}
			if (current - d >= 1 && !visited[current - d]) {
				que.offer(new int[] {current - d, cnt + 1});
				visited[current - d] = true;
			}
		}
	}
}
