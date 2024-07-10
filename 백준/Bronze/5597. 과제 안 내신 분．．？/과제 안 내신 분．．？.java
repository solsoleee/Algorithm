import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int arr[] = new int[31];
		
		Scanner sc = new Scanner(System.in);
		
		for(int i=0; i<28; i++) {
			int a = sc.nextInt();
			arr[a]=1;
		}
		
		for(int j=1; j<31; j++) {
			if (arr[j]!=1) System.out.println(j);
		}
		
		
		
		
	}

}