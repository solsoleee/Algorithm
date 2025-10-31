import java.io.*;
import java.util.*;

public class Main {
    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine()); // 편의점 개수
            
            Point[] points = new Point[n + 2]; // 집 + 편의점들 + 페스티벌
            
            // 집 좌표
            StringTokenizer st = new StringTokenizer(br.readLine());
            points[0] = new Point(Integer.parseInt(st.nextToken()), 
                                 Integer.parseInt(st.nextToken()));
            
            // 편의점 좌표들
            for (int i = 1; i <= n; i++) {
                st = new StringTokenizer(br.readLine());
                points[i] = new Point(Integer.parseInt(st.nextToken()), 
                                     Integer.parseInt(st.nextToken()));
            }
            
            // 페스티벌 좌표
            st = new StringTokenizer(br.readLine());
            points[n + 1] = new Point(Integer.parseInt(st.nextToken()), 
                                      Integer.parseInt(st.nextToken()));
            
            // BFS로 도달 가능한지 확인
            if (bfs(points, n)) {
                System.out.println("happy");
            } else {
                System.out.println("sad");
            }
        }
    }
    
    static boolean bfs(Point[] points, int n) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n + 2];
        
        queue.offer(0); // 집에서 시작
        visited[0] = true;
        
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            
            // 페스티벌 도착!
            if (cur == n + 1) {
                return true;
            }
            
            // 현재 위치에서 갈 수 있는 모든 곳 탐색
            for (int next = 0; next < n + 2; next++) {
                if (!visited[next] && canGo(points[cur], points[next])) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }
        
        return false; // 페스티벌에 도달 못함
    }
    
    // 두 지점 사이를 갈 수 있는지 (거리 1000m 이하)
    static boolean canGo(Point p1, Point p2) {
        int distance = Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
        return distance <= 1000;
    }
}