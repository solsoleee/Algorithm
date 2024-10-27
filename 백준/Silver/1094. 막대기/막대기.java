import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static StringTokenizer tokens;
    static int x;
    static PriorityQueue<Integer> pq;
    static List<Integer> stick;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        x = Integer.parseInt(input.readLine());
        pq = new PriorityQueue<>();
        stick = new ArrayList<>();
        stick.add(64);
        pq.add(64);
        int res = 0;
        if(stickSum() == x) {
            res = stick.size();
        }
        // stick의 합이 x보다 클 떄만 반복
        while(stickSum() > x) {
            Collections.sort(stick);
            //가장 길이가 짧은 것을 절반으로 자름
            int first = stick.remove(0);
            int half = first/2;
            if(stickSum() + half <x) {
                stick.add(half); //하나는 버림
            }
            stick.add(half);
            //남아있는 모든 막대를 풀로 붙여서 x를 만듦
            if(stickSum() == x) {
                res = stick.size();
                break;
            }
        }
        System.out.println(res);
    }
    static int stickSum() {
        int sum =0;
        for(int i=0; i<stick.size(); i++) {
            sum += stick.get(i);
        }
        return sum;
    }
}