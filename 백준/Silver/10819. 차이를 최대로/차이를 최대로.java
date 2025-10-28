

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int n;

	static int arr[];
	static int res[];
	static int ans = Integer.MIN_VALUE;
	static boolean visited[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		arr = new int[n];
		res = new int[n];
		visited = new boolean[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		permu(0);
		System.out.println(ans);

	}

	//순서 순열
	static void permu(int depth) {
		if (depth == n) {
			int c = cal();
			ans = Math.max(c, ans);
			return;
		}
		for (int i = 0; i < n; i++) {
			if (!visited[i]) {
				res[depth] = arr[i];
				visited[i] = true;
				permu(depth + 1);
				visited[i] = false;
			}
		}
	}

	// sum에서 가장 큰 수를 구하는 최댓값
	static int cal() {
		int sum = 0;
		for (int i = 0; i < n - 1; i++) {
			sum += Math.abs(res[i] - res[i + 1]);
		}
		return sum;
	}
}