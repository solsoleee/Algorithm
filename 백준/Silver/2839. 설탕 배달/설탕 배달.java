import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer tokens;
    private static int n;
    public static void main(String[] args) throws IOException {
        int cnt=0;
        n = Integer.parseInt(input.readLine());
        while(n > 0){
            if(n%5==0) {
                cnt+= n/5;
                n = n%5;
                break;
            }
            n-=3;
            cnt++;
        }
        if(n==0){
            System.out.print(cnt);
        }
        else{
            System.out.print(-1);
        }

    }
}