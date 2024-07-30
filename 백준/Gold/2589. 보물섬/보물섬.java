import java.io.*;
import java.util.*;
public class Main {
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer tokens;

	static char map[][];
	private static boolean visited[][];
	private static int deltas[][] = {{0,1},{1,0}, {-1,0}, {0,-1}};
	private static int max_value=Integer.MIN_VALUE;
	
	private static int c, r, cnt, dx, dy;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		tokens = new StringTokenizer(input.readLine());
		r = Integer.parseInt(tokens.nextToken());
		c = Integer.parseInt(tokens.nextToken());
		
		map = new char[r][c];
		for(int i=0; i<r; i++) {
			tokens = new StringTokenizer(input.readLine());
			String temp=tokens.nextToken();
			for(int j=0; j<c; j++) {
				map[i][j]=temp.charAt(j);
			}
		}
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				if(map[i][j] =='L') {
					max_value = Math.max(max_value, bfs(i,j,0));
				}
			}
		}
		System.out.println(max_value);
	}

	private static int bfs(int x, int y, int cnt) {
		Queue<int[]>que =new LinkedList<>();
		visited =new boolean[r][c];
		que.offer(new int[] {x,y,cnt});
        visited[x][y]=true;
		int max_distance=0;
		while(!que.isEmpty()) {
			int t[] = que.poll();
			x = t[0];
			y = t[1];
			cnt = t[2];
			
			max_distance = Math.max(max_distance, cnt);
			
			for(int d[]: deltas) {
				int nx = x+d[0];
				int ny = y+d[1];
				
				if(nx>=0 && nx<r && ny>=0 && ny<c) {
					if(!visited[nx][ny]) {
						if(map[nx][ny]=='L') {
							que.offer(new int [] {nx, ny, cnt+1});
							visited[nx][ny]=true;
						}
						
					}
				}
			}
		}
		return max_distance; //현재 점 중에 가장 큰 값
	}

}