import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Scanner sc =new Scanner(System.in);

        int n = sc.nextInt();
        int m =sc.nextInt();
        int arr[] = new int[n];
        
        for(int i=0; i<m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            
            for(int j=(a-1); j<b; j++) {
            	arr[j]=c;
            }    
        }
        
        for(int i=0; i<n; i++) {
        	System.out.print(arr[i] + " ");
        }

        sc.close();
		
		
	}

}