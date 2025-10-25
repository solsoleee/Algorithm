import java.util.*;

class Solution {
    int[] nums;
    int target, n, answer;

    public int solution(int[] numbers, int targets) {
        nums = numbers;
        target = targets;
        n = numbers.length;
        answer = 0;
        dfs(0, 0);                 
        return answer;
    }

    void dfs(int idx, int sum) {
        if (idx == n) {
            if (sum == target) answer++;
            return;
        }
        dfs(idx + 1, sum + nums[idx]);   // 현재 숫자에 +
        dfs(idx + 1, sum - nums[idx]);   // 현재 숫자에 -
    }
}
