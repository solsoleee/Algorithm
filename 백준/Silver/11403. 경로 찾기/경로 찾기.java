

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static List<Integer>[] graph;
	static boolean visited[];
	static int map[][];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		graph = new ArrayList[n + 1];
		map = new int[n + 1][n + 1];
		for (int i = 0; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				int num = Integer.parseInt(st.nextToken());

				if (num == 1) {
					graph[i].add(j);
				}

			}
		}
		//System.out.println(Arrays.toString(graph));

		for (int i = 1; i <= n; i++) {
			bfs(i);
		}

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {

				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
	}

	static void bfs(int x) {
		//1부터 시작
		Queue<Integer> que = new ArrayDeque<>();
		que.offer(x);
		visited = new boolean[n + 1];
		//visited[x] = true;
		while (!que.isEmpty()) {
			int num = que.poll();
			int s = graph[num].size();
			for (int i = 0; i < s; i++) {
				if (!visited[graph[num].get(i)]) {
					map[x][graph[num].get(i)] = 1;
					que.offer(graph[num].get(i));
					visited[graph[num].get(i)] = true;
				}

			}
		}
	}
}
