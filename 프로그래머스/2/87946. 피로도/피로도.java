import java.util.*;
class Solution {
    static int n;
    static int[][] dungeons;
    static boolean[] visited;
    static int [] res;
    static int energy;
    static int answer = Integer.MIN_VALUE;
    public int solution(int k, int[][] dungeonsInput) {
        
        energy = k;
        dungeons = dungeonsInput;
        n = dungeons.length;
        visited = new boolean[n];
        res = new int[n];
        
        
        permu(0);
        
        return answer;
    }
    
    static int cal(int seq[]) {
        int hp = energy;
        int cnt = 0;
        for(int s: seq) {
            if(dungeons[s][0] <= hp) { //최소 필요 피로도
                hp-= dungeons[s][1];
                if(hp >=0 ) cnt++;
            }
        }
        return cnt;
    }
    
    static void permu(int depth) {
        if(depth == n){
            //피로도 계산
            //System.out.println(Arrays.toString(res));
            int c = cal(res);
            answer = Math.max(answer, c);
            //System.out.println(c);
            return;
        }
        for(int i=0; i<n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                res[depth] = i;
                permu(depth+1);
                visited[i] = false;
            }
        }
    }
}