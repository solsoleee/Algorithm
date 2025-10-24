import java.util.*;

class Solution {

    static boolean visited[];
    static int len;
    static int answer = Integer.MAX_VALUE;
    static boolean flag;
    public int solution(String begin, String target, String[] words) {

        len = words.length;
        visited = new boolean [len];
        bfs(begin, target, words);
        if(!flag) return 0;
        else return answer;
        
    }
    static void bfs(String begin, String target, String[] words) {
        Queue<String[]> que = new ArrayDeque<>();
        
        que.offer(new String[]{begin,"0"});
        flag = false;
        while(!que.isEmpty()) {
            String temp[] = que.poll();
             String w = temp[0];
             int cnt = Integer.parseInt(temp[1]);
            
            if(w.equals(target)) {
                answer = Math.min(answer, cnt);
                flag = true; //변환할 수 있음
            }
            //한글자씩 바뀌는거 넣기
            for(int i=0; i<len; i++) {
                int l = temp[0].length();
                int same = 0; //다른 개수
                if(!visited[i]) {
                    for(int j=0; j<l; j++ ) {
                        if(temp[0].charAt(j) != words[i].charAt(j)) {
                            same++;
                        }
                        if(same > 2) break;
                    }
                    if(same == 1) {
                        que.offer(new String[]{words[i], String.valueOf(cnt+1)});
                        visited[i] = true;
                    }
                }
            }
        }
    }
    
    //bfs로 1단어가 다른지 판단 후, visited도 하고, cnt+1하고 
}