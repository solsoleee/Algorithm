import java.util.*;
class Solution {
    static int nums[];
    static int target;
    static int answer;
    static int n;
    public int solution(int[] numbers, int targets) {
        answer = 0;
        nums = numbers;
        target = targets;
        n = numbers.length;
        dfs(0,0,0);
        return answer;
    }
    static void dfs(int cnt, int sum, int start) {
        if(cnt == n) {
            if(sum == target) answer++; //같으면
            return; 
        }
        for(int i=start; i<n; i++) {
            dfs(cnt+1, sum+nums[i], i+1);
            dfs(cnt+1, sum-nums[i], i+1);
        }
    }
}