import java.util.*;
import java.io.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        int n = clothes.length;
        for(int i=0; i<n; i++) {
            String k = clothes[i][1];
            String v = clothes[i][0];
            map.put(k, map.getOrDefault(k,0)+1);
        }
        
        int sum=1;
        System.out.print(map.keySet());
        for(String k: map.keySet()) {
            sum = sum* (map.get(k) +1);
        }
        sum-=1;

        //int answer = 0;
        return sum;
    }
}