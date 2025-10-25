import java.util.*;
import java.io.*;

public class Main {
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer tokens;

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        long h = Long.parseLong(tokens.nextToken());
        long w = Long.parseLong(tokens.nextToken());
        long n = Long.parseLong(tokens.nextToken());
        long m = Long.parseLong(tokens.nextToken());

        long r = (h + (n + 1) - 1) / (n + 1); // = ceil(h/(n+1))
        long c = (w + (m + 1) - 1) / (m + 1); // = ceil(w/(m+1))

        System.out.println(r * c);
    }
}
