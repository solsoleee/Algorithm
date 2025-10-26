import java.util.*;
class Solution {
    static List<Integer> [] graph;
    static boolean [] visited;
    static int answer = Integer.MAX_VALUE;
    static int cnt;
    public int solution(int n, int[][] wires) {
  
        for(int k=0; k<wires.length; k++) {
            visited = new boolean[101];
            graph = new ArrayList [101];
            for(int j=0; j<101; j++) {
                graph[j] = new ArrayList<>();
            }
            for(int i=0; i<n-1; i++) {
                if(k!=i) {
                    graph[wires[i][0]].add(wires[i][1]);
                    graph[wires[i][1]].add(wires[i][0]);
                }
            }
            
                //System.out.println(Arrays.toString(graph));
                cnt=1;
                dfs(wires[k][0]);
                int a = cnt;
                cnt=1;
                dfs(wires[k][1]);
                int b = cnt;
                //System.out.println(a+" " +b);
                answer = Math.min(answer, Math.abs(a-b));
        }


        return answer;
    }
    //w에 따라 몇개 송신탑 있는지 세는 함수
    static void dfs(int w) {
        visited[w] = true;
        for(int i=0; i<graph[w].size(); i++) {
            int num = graph[w].get(i);
            if(!visited[num]) {
                visited[num] = true;
                cnt++;
                dfs(num);
            }
        }
    }
}