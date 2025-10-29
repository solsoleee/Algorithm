

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		Map<String, Integer> map = new HashMap<>();
		int n = Integer.parseInt(st.nextToken());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String str = st.nextToken();
			int idx = 0;
			for (int j = 0; j < str.length(); j++) {
				if (str.charAt(j) == '.') {
					idx = j + 1;
					break;
				}
			}
			str = str.substring(idx, str.length());
			map.put(str, map.getOrDefault(str, 0) + 1);
		}
		//map 정렬
		//string으로 정렬
		List<String> list = new ArrayList<>(map.keySet());
		Collections.sort(list);

		for (String l : list) {
			System.out.println(l + " " + map.get(l));
		}
	}
}
