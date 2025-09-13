import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int n = sequence.length;
        long dp[][] = new long[n][2];
        
        dp[0][0] = sequence[0]; // +1
        dp[0][1] = -sequence[0]; //-1
        
        for(int i=1; i<n; i++) {
            dp[i][0] = Math.max(0, dp[i-1][1]) + sequence[i];
            dp[i][1] = Math.max(0, dp[i-1][0]) - sequence[i];
        }
        for(long d[]:dp) {
            answer = Math.max(answer, Math.max(d[0],d[1]));
        }
        
        return answer;
    }
}