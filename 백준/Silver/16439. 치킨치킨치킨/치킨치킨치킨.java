

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n, m;

	static int arr[][];
	static int res[];
	static int ans = Integer.MIN_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		res = new int[3];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		//System.out.println(Arrays.deepToString(arr));
		combi(0, 0);
		System.out.println(ans);
	}

	static void combi(int start, int depth) {
		if (depth == 3) {
			// 가장 큰 값 선호도가

			int sum = 0;

			for (int i = 0; i < n; i++) {
				int max = 0;
				for (int j = 0; j < 3; j++) {
					int chicken = res[j];
					max = Math.max(arr[i][chicken], max); //각 시킨중에 제일 선호도 높은거
				}
				sum += max;
			}
			
			ans = Math.max(ans, sum);
			return;
		}
		for (int i = start; i < m; i++) {
			res[depth] = i;
			combi(i + 1, depth + 1);
		}
	}
}
