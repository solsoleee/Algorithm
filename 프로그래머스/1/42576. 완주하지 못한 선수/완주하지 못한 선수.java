import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        //completion를 map에 담고 participant로 키로 사용해서 포함하지 않은거 리턴
        Map <String, Integer> map = new HashMap<>();
        for(String s: completion) {
            map.put(s, map.getOrDefault(s, 0)+1);
        }
        
        // 있는지 없는지 확인
        for(String s: participant) {
            if(!map.containsKey(s)) {
                return s;
            }
            if(map.get(s)<=0) return s;
            //있으면 1을 빼줌, 없애줌?
            map.put(s, map.getOrDefault(s,0)-1);
            //System.out.println(map);
        }
        
        
        return answer;
    }
}