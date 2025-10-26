import java.util.*;
class Solution {
    static int cnt;
    static String w;
    static boolean flag;
    static int answer;
    static String arr[] = {"A","E","I","O","U"};
    public int solution(String word) {
        answer = 0;
        w = word;
        dfs("");
        return answer;
    }
    static void dfs(String s) {
        if(flag) return;
        if(s.length()>0) {
            cnt++;
            System.out.println(s);
            if(s.equals(w)) {
                flag = true;
                answer = cnt;
                return;
            }
        }
        if(s.length()==5) return;
        for(int i=0; i<5; i++) {
            dfs(s+arr[i]);
            if(flag) return;
        }
    }
}