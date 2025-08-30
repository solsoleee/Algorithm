import java.util.*;

class Solution {
    public long solution(int r1, int r2) {
        long R1 = r1, R2 = r2;

        // 1사분면(축 포함)의 점 개수: x >= 0, y >= 0
        long quad = 0;
        for (long x = 0; x <= R2; x++) {
            long yMax = (long) Math.floor(Math.sqrt(R2 * R2 - x * x));
            long minSq = R1 * R1 - x * x;
            long yMin = (minSq > 0) ? (long) Math.ceil(Math.sqrt(minSq)) : 0;
            if (yMax >= yMin) quad += (yMax - yMin + 1);
        }

        // 축 점 과계산 보정:
        // (x,0) (x>0) 과 (0,y) (y>0)은 실제로 각 2개(±)만 존재하는데,
        // 1사분면을 *4 하면 4번 계산되어 +2씩 과계산됨.
        long axisPos = Math.max(0, R2 - Math.max(1, R1) + 1); // 양의축 쪽 (x>0, y=0) 또는 (x=0, y>0) 개수
        long over = 2 * (axisPos + axisPos);                  // 두 축 모두에 대해 +2씩
        if (R1 == 0) over += 3;                               // 원점(0,0)은 *4 시 +3 과계산

        long answer = quad * 4 - over;
        return answer;
    }
}
