import java.util.*;
import java.io.*;
public class Main {
	static StringTokenizer tokens;
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static boolean [][] relation;

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(input.readLine()) + 1;
		relation = new boolean[n][n];
		while (true) {
			tokens = new StringTokenizer(input.readLine());
			int a = Integer.parseInt(tokens.nextToken());
			int b = Integer.parseInt(tokens.nextToken());
			if (a == -1 && b == -1) break;
			relation[a][b] = true;
			relation[b][a] = true;
		}
		bfs();
	}

	static void bfs() {
		int[] res = new int[n]; // 후보자
		int cnt = 0;
		int minScore = Integer.MAX_VALUE;

		for (int i = 1; i < n; i++) {
			int[] score = new int[n];
			Arrays.fill(score, -1);
			Queue<Integer> que = new LinkedList<>();
			que.add(i);
			score[i] = 0;

			while (!que.isEmpty()) {
				int current = que.poll();

				for (int j = 1; j < n; j++) {
					if (relation[current][j] && score[j] == -1) {
						que.add(j);
						score[j] = score[current] + 1;
					}
				}
			}

			int maxScore = Arrays.stream(score).max().getAsInt();
			if (maxScore > minScore) continue;

			if (maxScore < minScore) {
				minScore = maxScore;
				cnt = 0;
			}
			res[cnt++] = i;
		}

		System.out.println(minScore + " " + cnt);
		Arrays.sort(res, 0, cnt);
		for (int i = 0; i < cnt; i++) {
			System.out.print(res[i] + " ");
		}
	}
}