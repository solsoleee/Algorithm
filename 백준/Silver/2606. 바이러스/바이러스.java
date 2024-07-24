import java.io.*;
import java.util.*;

public class Main {

	
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	private static int cnt;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		int c = Integer.parseInt(input.readLine());
		int num = Integer.parseInt(input.readLine());
		
		int arr[][] =new int[c+1][c+1]; //컴퓨터의 개수
		boolean visited[] = new boolean[c+1]; //방문 처리
		
		
		for(int i=0; i<num; i++) {
			tokens = new StringTokenizer(input.readLine());
			int a = Integer.parseInt(tokens.nextToken());
			int b = Integer.parseInt(tokens.nextToken());
			arr[a][b]=1; //1은 연결 되어있는거
			arr[b][a]=1; 
			
		}
		
		////////자바에서 queue구현하기
		List<Integer> que = new LinkedList<Integer>();
		
		que.add(1);
		visited[1]=true;
		while(que.size()>0) {
			int x = que.get(0); //현재 
			que.remove(0);
			for(int i=0; i<=c; i++) {
				if(arr[x][i]==1 && visited[i]==false) { //연결되어 있고 방문하지 않았으면
					cnt++;
					que.add(i);
					visited[i]=true;
				}
			}
		}
		System.out.println(cnt);
		
		
	
	}

}