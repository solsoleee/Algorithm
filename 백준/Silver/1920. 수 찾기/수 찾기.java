

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int m;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int arrA[] = new int[n];

		for (int i = 0; i < n; i++) {
			arrA[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());

		m = Integer.parseInt(st.nextToken());
		int arrB[] = new int[m];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			arrB[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arrA);
		//이진탐색
		// 0~m까지 확인
		for (int i = 0; i < m; i++) {
			int target = arrB[i]; //목표
			boolean flag = false;
			int left = 0; //인덱스임
			int right = n - 1;

			while (left <= right) {
				int mid = (left + right) / 2;
				if (arrA[mid] > target) {
					right = mid - 1;
				} else if (arrA[mid] == target) {
					flag = true;
					break;
				} else
					left = mid + 1;
			}
			if (flag)
				System.out.println(1);
			else
				System.out.println(0);
		}

	}
}
