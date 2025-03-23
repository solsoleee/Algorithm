import java.util.*;
import java.io.*;
class Solution {
    public int solution(int n) {
        int dp[] = new int[100001];
        dp[0] = 0;
        dp[1] = 1;
        for(int i=2; i<=n; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) %1234567;
        }
        return dp[n];
        
    }
    
    // static int fibo (int n) {
    //     if(n==0) return 0;
    //     else if(n==1) return 1;
    //     else return fibo(n-1) + fibo(n-2);
    // }
}