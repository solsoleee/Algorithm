import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int n, l, r, x;
	static int res[];
	static int arr[];
	static boolean visited[];
	static int cnt;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		x = Integer.parseInt(st.nextToken());
		arr = new int[n];
		res = new int[n];
		visited = new boolean[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		subSet(0);
		System.out.println(cnt);
	}

	//부분집합만들기
	static void subSet(int depth) {
		if (depth == n) {

			if (check()) {
				cnt++;
			}

			return;
		}
		//선택해도 되고 안 선택해도 되고
		visited[depth] = true;
		subSet(depth + 1);

		visited[depth] = false;
		subSet(depth + 1);

	}

	//문제
	static boolean check() {
		int max_val = 0;
		int min_val = 1000001;
		int sum = 0;
		//두문제 이상이어야함
		int c = 0;
		for (int i = 0; i < n; i++) {
			if (visited[i]) {
				c++;
				max_val = Math.max(max_val, arr[i]);
				min_val = Math.min(min_val, arr[i]);
				sum += arr[i];
			}
		}
		if (c < 2)
			return false;

		if (sum >= l && sum <= r) {
			if (max_val - min_val >= x) {
				return true;
			}
		}
		return false;
	}

}
