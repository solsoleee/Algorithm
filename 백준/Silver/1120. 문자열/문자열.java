

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class  Main {
	static String a, b;
	static int ans = Integer.MAX_VALUE;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		a = st.nextToken();
		b = st.nextToken();

		int len = b.length() - a.length();
		for (int i = 0; i < len + 1; i++) {
			int c = check(i);
			ans = Math.min(c, ans);
		}
		System.out.println(ans);

	}

	static int check(int start) {
		//b는 출발점이 start
		int cnt = 0;
		for (int i = 0; i < a.length(); i++) {
			if (a.charAt(i) != b.charAt(i + start)) {
				cnt++;
			}
		}
		return cnt;
	}

}
