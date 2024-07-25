import java.io.*;
import java.util.*;


public class Main {

	
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output1 = new StringBuilder();
	private static StringBuilder output2 = new StringBuilder();
	private static StringTokenizer tokens;
	private static int graph[][];
	private static boolean bfs_visited[];
	private static boolean dfs_visited[];
	private static int n,m,v;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		tokens = new StringTokenizer(input.readLine());
		n = Integer.parseInt(tokens.nextToken());
		m = Integer.parseInt(tokens.nextToken());
		v = Integer.parseInt(tokens.nextToken());
		
		graph = new int [n+1][n+1];
		bfs_visited = new boolean[n+1];
		dfs_visited = new boolean[n+1];
		
		for(int i=0; i<m; i++) {
			tokens = new StringTokenizer(input.readLine());
			int a = Integer.parseInt(tokens.nextToken());
			int b = Integer.parseInt(tokens.nextToken());
			graph[a][b] = 1;
			graph[b][a] = 1;
		}

		//bfs 구현
		List<Integer> que = new LinkedList<Integer>();
		
		que.add(v);
		bfs_visited[v]=true;
		
		while(que.size()>0) {
			int x = que.get(0); //현재 
			output1.append(x).append(" ");
			que.remove(0);
			for(int i=1; i<=n; i++) {
				if(graph[x][i]==1 && bfs_visited[i]==false) {
					que.add(i);
					bfs_visited[i]=true;
				}
			}
			
		}
		dfs(v);
		System.out.println(output2);
		System.out.println(output1);
	
	} //main 끝
	
	
	//dfs 구현
	static void dfs(int v) {
		Stack<Integer> stack = new Stack<Integer>();
		stack.add(v);
		output2.append(v).append(" ");
		dfs_visited[v]=true;
		for(int i=1; i<=n;i++) {
			if(graph[v][i]==1 && dfs_visited[i]==false) {
				dfs(i);

			}
		}		
	}
}