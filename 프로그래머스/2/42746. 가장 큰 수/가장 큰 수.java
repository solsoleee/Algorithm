import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // 1) 숫자를 문자열로
        String[] a = Arrays.stream(numbers)
                           .mapToObj(String::valueOf)
                           .toArray(String[]::new);

        // 2) (b+a) vs (a+b) 비교로 내림차순 정렬
        Arrays.sort(a, (x, y) -> (y + x).compareTo(x + y));

        // 3) 모두 0이면 "0"
        if (a[0].equals("0")) return "0";

        // 4) 이어 붙이기
        StringBuilder sb = new StringBuilder();
        for (String s : a) sb.append(s);
        return sb.toString();
    }
}
