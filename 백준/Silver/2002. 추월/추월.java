
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		Map<String, Integer> map = new HashMap<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			map.put(st.nextToken(), i + 1); //이름과 순위
		}
		//System.out.println(map);
		//다시 순위 또 확인
		int cnt = 0;
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			String name = st.nextToken();
			int rank = map.get(name);
			//현재 인덱스랑 rank랑 다르면
			if (i != rank) {
				cnt++;
				//현재 name말고 다른거 다 +1
				for (String s : map.keySet()) {
					if (!s.equals(name)) {
						//본인보다 위의 순위만 영향
						if (rank > map.get(s)) {
							map.put(s, map.get(s) + 1);
						}

					}
				}
				map.put(name, i);
			}
			//System.out.println(map);
		}

		System.out.println(cnt);
	}

}
