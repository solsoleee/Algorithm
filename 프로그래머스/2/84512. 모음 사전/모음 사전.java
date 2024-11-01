import java.util.*;
class Solution {
    static String str[] = {"A","E","I","O","U"};
    static List<String> list;
    public int solution(String word) {
        list = new ArrayList<>();
        dfs(0,"");
        int answer = 0;
        for(int i=0; i<list.size(); i++) {
            if(list.get(i).equals(word)) {
                answer = i;
                break;
            }
        }
    
        
        return answer;
    }
    static void dfs(int cnt, String words) {
        list.add(words);
        if(cnt == 5) {
            return;
        }
        for(int i=0; i<5; i++) {
            dfs(cnt+1, words + str[i]);
        }
    }
}