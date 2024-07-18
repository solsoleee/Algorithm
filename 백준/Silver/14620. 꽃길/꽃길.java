import java.awt.Checkbox;
import java.io.*;
import java.util.*;

public class Main {

	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	
	private static int deltas[][] = {{-1,0},{1,0},{0,-1},{0,1}};
	private static int cnt;
	private static int cost=Integer.MAX_VALUE;
	private static int n;
	private static int graph[][];
	private static boolean visited[][];
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		n = Integer.parseInt(input.readLine());
		graph= new int[n][n];
		visited= new boolean[n][n];
		
		//graph만들
		for(int i=0; i<n; i++) {
			tokens = new StringTokenizer(input.readLine());
			for(int j=0; j<n; j++) {
				graph[i][j] = Integer.parseInt(tokens.nextToken());
			}
		}
		dfs(0,0);
		System.out.println(cost);
	}
	
	
	private static void dfs(int cnt, int sum) {
		if(cnt==3) {
			cost=Math.min(cost, sum);
			return ;
		}

		for(int i=1; i<n-1; i++) {
			for(int j=1; j<n-1; j++) {
				if(check(i, j)) {
					int total = graph[i][j];
					visited[i][j]=false;
					for(int d=0; d<4; d++) {
						int nx = i+deltas[d][0];
						int ny = j+deltas[d][1];
						total+=graph[nx][ny];
						visited[nx][ny]=true;
					}
					dfs(cnt+1, sum+total);
					visited[i][j]=false;
					for(int d=0; d<4; d++) {
						int nx = i+deltas[d][0];
						int ny = j+deltas[d][1];
						visited[nx][ny]=false;
					}
				}	
			}
		}
	}
	
	private static boolean check(int x, int y) {
		if(visited[x][y]) {
			return false;
		}
		for(int d[]: deltas) {
			int nx = x+d[0];
			int ny = y+d[1];
			if(visited[nx][ny]) return false;
		}
		return true;
	}
	
	
}