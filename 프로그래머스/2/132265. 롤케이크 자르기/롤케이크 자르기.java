import java.util.*;
class Solution {
    public int solution(int[] topping) {
        int len = topping.length;
        Set<Integer> set = new HashSet<>();
        Map<Integer, Integer> map = new HashMap<>();
        int answer = 0;
        for(int t :topping) {
            map.put(t, map.getOrDefault(t,0)+1);
        }
        
        //하나씩 꺼내면서 탐색
        for(int i=0; i<len; i++) {
            set.add(topping[i]);
            map.put(topping[i], map.get(topping[i])-1);
            if(map.get(topping[i]) == 0) map.remove(topping[i]);
            if(map.size() == set.size()) answer++;
        }
        
        
        return answer;
    }
}