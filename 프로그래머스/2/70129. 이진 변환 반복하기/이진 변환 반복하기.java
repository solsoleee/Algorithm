import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int res = 0;
        while(!s.equals("1")) {
            int n = s.length();
            int c = count(s); //1의 개수
            answer[1] += (n-c); // 제거할 0의 개수
            s = change(c); //2진수로 변환
            res ++;
            
        }
        answer[0] = res;
        return answer;
    }
    
    static int count(String str) {
        int cnt = 0;
        for(int i=0; i<str.length(); i++) {
            if(str.charAt(i) == '1') cnt++;
        }
        return cnt;
        
    }
    
    static String change(int n) {
        //n이 1이 될때까지
        //0이 개수만 고르면 되는거라서 순서는상관X
        String c ="";
        while(n != 1) {
            c += Integer.toString(n%2);
            n = n/2;  
        }
        c+=n;
        return c;
        //System.out.println(n);
    }
    
}