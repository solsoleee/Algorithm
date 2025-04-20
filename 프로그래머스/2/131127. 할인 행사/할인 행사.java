import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        // 1. wantMap 만들기
        Map<String, Integer> wantMap = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }

        // 2. 슬라이딩 윈도우 (10일)
        for (int i = 0; i <= discount.length - 10; i++) {
            Map<String, Integer> saleMap = new HashMap<>();
            for (int j = i; j < i + 10; j++) {
                saleMap.put(discount[j], saleMap.getOrDefault(discount[j], 0) + 1);
            }

            // 3. wantMap과 일치하는지 비교
            if (saleMap.equals(wantMap)) {
                answer++;
            }
        }

        return answer;
    }
}
