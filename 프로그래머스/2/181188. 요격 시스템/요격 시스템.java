import java.util.*;
import java.io.*;
class Solution {
    public int solution(int[][] targets) {
        //끝점이 작은 거대로 정렬
        Arrays.sort(targets, (a,b) -> a[1]-b[1]);
        //System.out.println(Arrays.deepToString(targets));
        int answer = 0;
        int end = 0;
        for(int i=0; i<targets.length; i++) {
            if(end <=targets[i][0]) {
                end = targets[i][1];
                answer++;
            }
        }
        
        return answer;
    }
}