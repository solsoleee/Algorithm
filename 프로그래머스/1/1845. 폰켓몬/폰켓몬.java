import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        // nums/2를 선택
        // 가장 종류가 많도록 선택
        // 종류의 최대값
        int len = nums.length;
        Set<Integer> set = new HashSet<>();
        for(int i=0; i<len; i++) {
            set.add(nums[i]);
        }
        System.out.println(set);
        // 종류가 많다면 최대값은 선택할 수 있는 수
        if(set.size() >= len/2 ) answer = len/2;
        else {
            answer = set.size();
        }
        return answer;
    }
}