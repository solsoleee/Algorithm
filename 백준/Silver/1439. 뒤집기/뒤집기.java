import java.util.Scanner;

public class Main {

	private static String str;
	private static int cnt0 =0, cnt1 =0;
	private static char pre;
	private static int min_value = Integer.MIN_VALUE;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		str = sc.nextLine();
		change0(str);
		change1(str);
		min_value = Math.min(cnt0, cnt1);
		System.out.println(min_value);
		
		
		
	}
	
	//0으로 바꾸는 함수
	private static void change0(String str) {
		pre=' ';
		for(int i=0; i<str.length(); i++) {
			char current = str.charAt(i);
			if(current!='0' && current!=pre) {
				cnt0++;
			}
			pre=str.charAt(i);//전에거 저장
		}
	}
	//1으로 바꾸는 함수
	private static void change1(String str) {
		pre=' ';
		for(int i=0; i<str.length(); i++) {
			char current = str.charAt(i);
			if(current!='1' && current!=pre) {
				cnt1++;
			}
			pre=str.charAt(i);//전에거 저장
		}
	}

}