import java.util.*;

class Solution {
    static boolean[] used;
    static List<String> path;
    static String[] answer;
    static String[][] tickets;
    static int n;

    public String[] solution(String[][] ticketsInput) {
        tickets = ticketsInput;
        n = tickets.length;
        used = new boolean[n];
        path = new ArrayList<>();

        // 1) 사전순 보장을 위해 (from, to) 기준 정렬
        Arrays.sort(tickets, (a, b) -> {
            if (!a[0].equals(b[0])) return a[0].compareTo(b[0]);
            return a[1].compareTo(b[1]);
        });

        // 2) 시작점 고정
        path.add("ICN");

        // 3) DFS: 첫 완성 경로를 찾으면 즉시 true 반환(사전순 최소 보장)
        dfs("ICN", 0);

        return answer;
    }

    static boolean dfs(String cur, int usedCnt) {
        if (usedCnt == n) {                 // 모든 티켓 사용 완료
            answer = path.toArray(new String[0]);
            return true;                    // 첫 경로가 사전순 최소
        }

        for (int i = 0; i < n; i++) {
            if (!used[i] && tickets[i][0].equals(cur)) {
                used[i] = true;

                // 이동: 도착지 추가
                path.add(tickets[i][1]);

                // 다음 공항으로 진행
                if (dfs(tickets[i][1], usedCnt + 1)) return true;

                // 백트래킹: 되돌리기
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
        return false;
    }
}
