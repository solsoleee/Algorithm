import java.io.*;
import java.util.*;

public class Main {
    private static StringTokenizer tokens;
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static int n, k;
    static int res[];
    static boolean visited[];
    static String strArr[];
    static Set<Character> essentialSet;
    static int maxVal = 0;

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        n = Integer.parseInt(tokens.nextToken());
        k = Integer.parseInt(tokens.nextToken());
        strArr = new String[n];
        
        // K가 5 미만이면 읽을 수 있는 단어는 없음
        if (k < 5) {
            System.out.println(0);
            return;
        }

        // 고정된 문자 a, n, t, i, c는 항상 포함됨
        essentialSet = new HashSet<>(Arrays.asList('a', 'n', 't', 'i', 'c'));
        visited = new boolean[26]; // 알파벳 체크
        res = new int[k - 5]; // a, n, t, i, c 제외한 문자 조합 저장용
        
        // 단어 입력받고 앞뒤 "anta"와 "tica"를 제거
        for (int i = 0; i < n; i++) {
            String str = input.readLine();
            strArr[i] = str.substring(4, str.length() - 4); // anta-와 -tica 제거
        }

        // 기본적으로 a, n, t, i, c는 선택된 상태로 시작
        visited['a' - 'a'] = true;
        visited['n' - 'a'] = true;
        visited['t' - 'a'] = true;
        visited['i' - 'a'] = true;
        visited['c' - 'a'] = true;

        combi(0, 0);
        System.out.print(maxVal);
    }

    // 조합
    static void combi(int start, int cnt) {
        if (cnt == k - 5) {
            int c = check();
            maxVal = Math.max(c, maxVal);
            return;
        }
        for (int i = start; i < 26; i++) {
            if (!visited[i]) {
                visited[i] = true;
                combi(i + 1, cnt + 1);
                visited[i] = false;
            }
        }
    }

    // 단어가 현재 선택된 문자로 읽을 수 있는지 체크
    static int check() {
        int count = 0;
        for (String s : strArr) {
            boolean canRead = true;
            for (int i = 0; i < s.length(); i++) {
                if (!visited[s.charAt(i) - 'a']) {
                    canRead = false;
                    break;
                }
            }
            if (canRead) count++;
        }
        return count;
    }
}