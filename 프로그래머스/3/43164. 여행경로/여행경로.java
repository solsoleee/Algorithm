import java.util.*;

class Solution {
    static String[][] tickets;
    static List<String> path;
    static boolean[] used;
    static String[] answer;
    static int n;

    public String[] solution(String[][] ticketsInput) {
        tickets = ticketsInput;
        n = tickets.length;
        used = new boolean[n];
        path = new ArrayList<>();

        // (1) from → to 오름차순
        Arrays.sort(tickets, (a, b) -> {
            int c = a[0].compareTo(b[0]);
            return (c != 0) ? c : a[1].compareTo(b[1]);
        });

        path.add("ICN");
        dfs(0, "ICN");   // (2) dfs가 boolean을 반환하도록

        return answer;
    }

    static boolean dfs(int cnt, String cur) {
        if (cnt == n) {                  // 모든 티켓 사용 완료
            answer = path.toArray(new String[0]);
            return true;                 // 첫 경로에서 즉시 종료
        }
        for (int i = 0; i < n; i++) {
            if (!used[i] && tickets[i][0].equals(cur)) {
                used[i] = true;
                path.add(tickets[i][1]);

                if (dfs(cnt + 1, tickets[i][1])) return true;  // 성공 전파

                // 백트래킹
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
        return false;
    }
}
