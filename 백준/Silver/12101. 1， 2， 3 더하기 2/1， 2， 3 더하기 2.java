

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int n, k;

	static int cnt;
	static boolean flag;

	static int res[];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		res = new int[n];
		permu(0, 0);
		if (!flag)
			System.out.println(-1);
	}

	//중복순열
	static void permu(int depth, int num) {
		if (num == n) {
			cnt++;
			if (cnt == k) {
				flag = true;
				for (int i = 0; i < depth; i++) {
					System.out.print(res[i]);
					if (i != depth - 1)
						System.out.print("+");
				}
			}
			return; //현재 수가 목표랑 같다면
		}

		for (int i = 1; i <= 3; i++) {
			int tempN = num + i;
			if (tempN > n)
				continue;
			res[depth] = i;
			permu(depth + 1, tempN);

		}

	}

}
