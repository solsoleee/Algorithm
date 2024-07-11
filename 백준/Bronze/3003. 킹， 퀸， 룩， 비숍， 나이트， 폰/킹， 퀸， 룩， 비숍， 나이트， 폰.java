import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int f [] = {1, 1, 2, 2, 2, 8};

		List<Integer> list = new ArrayList<>();
		
		String input[] = sc.nextLine().split(" ");
		for (int i=0; i<input.length; i++) {
			int a = Integer.parseInt(input[i]);
			list.add(f[i]-a);
		}
		
		for(int i : list) {
			System.out.print(i + " ");
		}
		
		
		sc.close();
	}
}