import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		sc.nextLine();
		String [] input = sc.nextLine().split("");
		int sum = 0;
		for (String i: input) {
			sum += Integer.parseInt(i);
		}
		
		System.out.println(sum);

		
		sc.close();
	}
}