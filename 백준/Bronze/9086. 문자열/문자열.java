import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        int N=sc.nextInt();
        sc.nextLine();
        for(int i=0; i<N; i++){
            String str = sc.nextLine();
            String str_list[] = str.split("");
            System.out.println(str_list[0]+str_list[str_list.length-1]);
        }
        sc.close();
    }
}

