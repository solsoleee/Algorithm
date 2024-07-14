import java.io.*;
import java.util.*;
public class Main {

	private static BufferedReader input  = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	
	
	public static void main(String[] args) throws IOException {
		
		Stack<Integer> stack = new Stack<>();
		
		int n = Integer.parseInt(input.readLine());
		for(int i=0; i<n; i++) {
			tokens=new StringTokenizer(input.readLine());
			switch(Integer.parseInt(tokens.nextToken())) {
			case(1):
				int s = Integer.parseInt(tokens.nextToken());
				stack.push(s);
				break;
			case(2):
				if (stack.isEmpty()) System.out.println(-1);
				else System.out.println(stack.pop()); 
				break;
			case(3):
				System.out.println(stack.size());
				break;
			case(4):
				if (stack.isEmpty()) System.out.println(1);
				else System.out.println(0);
				break;
			case(5):
				if (stack.isEmpty()) System.out.println(-1);
				else System.out.println(stack.peek());
				break;
			}
		}
	}

}