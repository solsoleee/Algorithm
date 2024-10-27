import java.util.*;

class Solution {
    static boolean visited[];
    static int n;
    static int arr[];
    static int answer;
    public int solution(int[] numbers, int target) {
        n = numbers.length;
        dfs(numbers, 0,0,target);
        return answer;
    }
    static void dfs(int[] numbers, int cnt, int sum, int target) {
        if(cnt == n) {
            if(sum == target) answer++;
            return;
        }
        dfs(numbers, cnt+1, sum+numbers[cnt],target);
        dfs(numbers, cnt+1, sum-numbers[cnt],target);
    }
}