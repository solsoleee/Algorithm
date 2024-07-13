import java.io.*;
import java.util.*;

public class Main {

	private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		int N = Integer.parseInt(input.readLine());
		int sum;
		boolean flag = true;
		for (int i=0; i<1000000; i++) {
			sum=0;
			String plus = String.valueOf(i);
			for (int j=0; j<plus.length(); j++) {
				sum+=Character.getNumericValue(plus.charAt(j));
			}
			sum+=i;
			if (N==sum) {
				System.out.println(i);
				flag = false;
				break;
			}
		}
		if (flag) System.out.println(0);
		
	}
	
	
	
	
}