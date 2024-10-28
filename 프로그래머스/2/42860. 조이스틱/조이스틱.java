import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;

        // 알파벳 변경 최소 횟수 계산
        for (int i = 0; i < name.length(); i++) {
            int up = name.charAt(i) - 'A';
            int down = 'Z' - name.charAt(i) + 1;
            answer += Math.min(up, down);
        }

        // 좌우 이동 최소 횟수 계산
        int length = name.length();
        int minMove = length - 1; // 오른쪽 끝까지 쭉 가는 경우
        
        for (int i = 0; i < length; i++) {
            int next = i + 1;

            // 연속된 'A' 구간 건너뛰기
            while (next < length && name.charAt(next) == 'A') {
                next++;
            }

            // 좌우 이동 거리 중 최솟값 찾기
            minMove = Math.min(minMove, i + length - next + Math.min(i, length - next));
        }

        answer += minMove;
        return answer;
    }
}
