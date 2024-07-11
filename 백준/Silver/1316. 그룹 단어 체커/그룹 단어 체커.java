import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		
		int n=sc.nextInt();
		sc.nextLine();
		int res=0;
		for(int i =0; i<n; i++) {
			boolean flag  = true ;
			String str = sc.nextLine();
			
			int arr [] =new int[26];
			char pre=str.charAt(0);
			for(int j=0; j<str.length(); j++) {
				if (pre!=str.charAt(j) && arr[str.charAt(j)-97]>=1) {
					flag = false;
					break;
			}
				arr[str.charAt(j)-97]++;
				pre=str.charAt(j);
			}
			if (flag) res+=1;
			
		}
		System.out.println(res);

		sc.close();
	}
}