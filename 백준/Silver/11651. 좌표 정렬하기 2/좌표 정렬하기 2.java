import java.io.*;
import java.util.*;
public class Main {

	private static BufferedReader input  = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder output = new StringBuilder();
	private static StringTokenizer tokens;
	

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int n = Integer.parseInt(input.readLine());
		int arr[][] = new int [n][2];
//		List<Integer> list = new ArrayList<Integer>();
		for (int i =0 ; i<n; i++) {
			tokens = new StringTokenizer(input.readLine());
			arr[i][0] = Integer.parseInt(tokens.nextToken());
			arr[i][1] = Integer.parseInt(tokens.nextToken());
		}
		Arrays.sort(arr, (a,b) -> {
			if (a[1]==b[1]) {
				return Integer.compare(a[0], b[0]);
			}
			else {
				return Integer.compare(a[1], b[1]);
			}	
	});
		
		for(int j =0; j<arr.length; j++) {
			output.append(arr[j][0]).append(" ").append(arr[j][1]).append("\n");
			
		}
		System.out.println(output);
	}

}