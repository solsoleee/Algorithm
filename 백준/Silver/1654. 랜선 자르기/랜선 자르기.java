import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int k, n;
    static StringTokenizer tokens;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static long [] lamp;
    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        k = Integer.parseInt(tokens.nextToken());
        n = Integer.parseInt(tokens.nextToken());
        lamp = new long[k];
        for(int i=0; i<k; i++) {
            lamp[i] = Long.parseLong(input.readLine());
        }
        Arrays.sort(lamp);
        long start = 1;
        long end = lamp[k-1];
        long res = 1;
        while(start <=end) {
            long mid = (start+end)/2;
            long ans = 0; //얻을 수 있는거
            for(int i=0; i<k; i++) {
                ans += lamp[i] / mid;
            }
            if(ans < n) { //더 적게 자르기
                end = mid-1;
            }
            else {
                start = mid+1;
                res = mid; //최대 랜선 길
            }
            //System.out.println(mid);
        }
        System.out.println(res);

    }
}