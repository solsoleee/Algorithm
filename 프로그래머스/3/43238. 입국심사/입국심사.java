import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        int len = times.length;
        Arrays.sort(times);
        
        long start = 0;
        long end = times[len-1] * (long)n;
        long answer = 0;
        
        while(start <= end) {
            
            long mid = (start + end) / 2; //최종 시간?
            long ans =0;
            for(int i=0; i<len; i++) {
                ans += mid / times[i];
            }
            if(ans < n) { //총 시간이 너무 적다는 것
                start = mid + 1;
            }
            else {
                end = mid -1;
                answer = mid;
            }
            
        }
        
        return answer;
    }
}