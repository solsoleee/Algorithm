import java.util.*;

public class Solution {
    public List solution(int []arr) {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        //연속적인거 하나만 넣음
        list.add(arr[0]);
        int pre = arr[0];
        for(int i=1; i<arr.length; i++) {
            if(pre == arr[i]) continue;
            else list.add(arr[i]);
            pre = arr[i];
        }
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        //System.out.println(list);

        return list;
    }
}