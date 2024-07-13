import java.io.*;
import java.util.StringTokenizer;

public class Main {

	
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

//		String str = input.readLine();
		int a = Integer.parseInt(input.readLine());
		int b = Integer.parseInt(input.readLine());
		int c = Integer.parseInt(input.readLine());
		String str = String.valueOf(a*b*c);
		String [] digits = str.split("");
		
		for(int i=0; i<10; i++) {
			int cnt =0 ;
			for(String d: digits) {
				if(i==Integer.parseInt(d)) cnt++;
			}
			System.out.println(cnt);
		}
	}

}