import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        int len = topping.length;
        //다 넣기
        for(int t: topping) {
            map.put(t, map.getOrDefault(t,0)+1);
        }
        for(int i=0; i<len; i++) {
            set.add(topping[i]);
            map.put(topping[i], map.getOrDefault(topping[i],0)-1);
            if(map.get(topping[i]) ==0 ) map.remove(topping[i]);
            if(map.size() == set.size()) answer ++;
        }
        
        return answer;
    }
}