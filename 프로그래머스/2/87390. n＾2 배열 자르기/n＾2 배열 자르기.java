import java.util.*;
class Solution {
    public int[] solution(int n, long left, long right) {
        long leftR = left/n;
        long leftC = left%n;
        long rightR = right/n;
        long rightC = right%n;
        int len =(int) (right-left) +1;
        int[] answer = new int[len];
        
        for(int i=0; i<answer.length; i++) {
            int idx = (int) Math.max(leftR, leftC);
            answer[i] = idx+1;
            if(leftC + 1 >= n ) {
                leftR++;
                leftC = (leftC+1)%n;
            }
            else leftC++;
        }
        
      
        
        
        return answer;
    }
}