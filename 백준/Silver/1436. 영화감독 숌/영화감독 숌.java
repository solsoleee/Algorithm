import java.util.*;
import java.io.*;
public class Main {
	
	
	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {

		
		int n = Integer.parseInt(input.readLine());
		
		
		int num = 666;
		int count =0; //답
		
		while (true) {
			
			if (String.valueOf(num).contains("666")){
				count++;
			}
			
			if (count==n) {
				System.out.println(num);
				break;
			}
			num++;
		}
			
		
		
		
	}

}