import java.util.*;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        int totalPicks = picks[0] + picks[1] + picks[2];
        int groups = Math.min((minerals.length + 4) / 5, totalPicks);

        // 1) 그룹 만들기: [dia, iron, stone]
        List<int[]> chunk = new ArrayList<>();
        int idx = 0;
        for (int g = 0; g < groups; g++) {
            int dia = 0, iron = 0, stone = 0;
            for (int t = 0; t < 5 && idx < minerals.length; t++, idx++) {
                String s = minerals[idx];
                if (s.equals("diamond")) dia++;
                else if (s.equals("iron")) iron++;
                else stone++;
            }
            chunk.add(new int[]{dia, iron, stone});
        }

        // 2) 그룹 난이도 기준 내림차순 정렬(돌 곡괭이 피로도)
        chunk.sort((a, b) -> {
            int wa = a[0]*25 + a[1]*5 + a[2];
            int wb = b[0]*25 + b[1]*5 + b[2];
            return Integer.compare(wb, wa);
        });

        // 3) 곡괭이 배정
        int fatigue = 0;
        for (int[] g : chunk) {
            if (picks[0] > 0) {                // diamond pick
                fatigue += g[0] + g[1] + g[2];
                picks[0]--;
            } else if (picks[1] > 0) {         // iron pick
                fatigue += g[0]*5 + g[1] + g[2];
                picks[1]--;
            } else {                            // stone pick
                fatigue += g[0]*25 + g[1]*5 + g[2];
                picks[2]--;
            }
        }
        return fatigue;
    }
}
