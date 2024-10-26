import java.util.*;
class Solution {
    public int solution(int n) {
        //n의 비트카운트로서 1의 개수 셈
        int res = Integer.bitCount(n);
        int answer = n+1;
        //System.out.println(res);
        while(true) {
            if(Integer.bitCount(answer) == res) {
                break;
            }
            answer++;
        }
        return answer;
    }
    

}