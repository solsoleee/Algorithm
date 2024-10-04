import java.util.*;

public class Solution {
    
    static class Position {
        int x1, y1, x2, y2, time;

        Position(int x1, int y1, int x2, int y2, int time) {
            this.x1 = x1;
            this.y1 = y1;
            this.x2 = x2;
            this.y2 = y2;
            this.time = time;
        }
    }

    public int solution(int[][] board) {
        int n = board.length;
        Position start = new Position(0, 0, 0, 1, 0);  // 로봇의 초기 위치
        Set<String> visited = new HashSet<>();  // 로봇이 방문했던 위치
        String initialPos = "0,0,0,1";  // 초기 위치를 문자열로 저장
        visited.add(initialPos);  // 방문처리

        int[] dx = {-1, 1, 0, 0};  // 상하좌우 이동
        int[] dy = {0, 0, -1, 1};  // 상하좌우 이동

        Queue<Position> queue = new LinkedList<>();
        queue.offer(start);

        while (!queue.isEmpty()) {
            Position pos = queue.poll();
            int x1 = pos.x1, y1 = pos.y1, x2 = pos.x2, y2 = pos.y2, time = pos.time;

            // 목표에 도달했을 때
            if ((x1 == n - 1 && y1 == n - 1) || (x2 == n - 1 && y2 == n - 1)) {
                return time;
            }

            // 상하좌우 이동
            for (int i = 0; i < 4; i++) {
                int nx1 = x1 + dx[i], ny1 = y1 + dy[i];
                int nx2 = x2 + dx[i], ny2 = y2 + dy[i];

                if (isValid(nx1, ny1, nx2, ny2, n, board) && !visited.contains(nx1 + "," + ny1 + "," + nx2 + "," + ny2)) {
                    visited.add(nx1 + "," + ny1 + "," + nx2 + "," + ny2);  // 방문처리
                    queue.offer(new Position(nx1, ny1, nx2, ny2, time + 1));
                }
            }

            // 회전
            if (x1 == x2) {  // 가로로 놓여있는 경우
                for (int i = -1; i <= 1; i += 2) {  // 위나 아래로 회전
                    if (isValid(x1 + i, y1, x2 + i, y2, n, board)) {
                        if (!visited.contains(x1 + "," + y1 + "," + (x1 + i) + "," + y1)) {
                            visited.add(x1 + "," + y1 + "," + (x1 + i) + "," + y1);
                            queue.offer(new Position(x1, y1, x1 + i, y1, time + 1));
                        }
                        if (!visited.contains(x2 + "," + y2 + "," + (x2 + i) + "," + y2)) {
                            visited.add(x2 + "," + y2 + "," + (x2 + i) + "," + y2);
                            queue.offer(new Position(x2, y2, x2 + i, y2, time + 1));
                        }
                    }
                }
            } else if (y1 == y2) {  // 세로로 놓여있는 경우
                for (int i = -1; i <= 1; i += 2) {  // 왼쪽이나 오른쪽으로 회전
                    if (isValid(x1, y1 + i, x2, y2 + i, n, board)) {
                        if (!visited.contains(x1 + "," + y1 + "," + x1 + "," + (y1 + i))) {
                            visited.add(x1 + "," + y1 + "," + x1 + "," + (y1 + i));
                            queue.offer(new Position(x1, y1, x1, y1 + i, time + 1));
                        }
                        if (!visited.contains(x2 + "," + y2 + "," + x2 + "," + (y2 + i))) {
                            visited.add(x2 + "," + y2 + "," + x2 + "," + (y2 + i));
                            queue.offer(new Position(x2, y2, x2, y2 + i, time + 1));
                        }
                    }
                }
            }
        }

        return -1;  // 목적지에 도달하지 못하면 -1 반환
    }

    // 두 위치가 유효한지 확인하는 함수
    private boolean isValid(int x1, int y1, int x2, int y2, int n, int[][] board) {
        return x1 >= 0 && y1 >= 0 && x2 >= 0 && y2 >= 0 && x1 < n && y1 < n && x2 < n && y2 < n
               && board[x1][y1] == 0 && board[x2][y2] == 0;
    }
}
