import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        String t = st.nextToken();

        int k;
        if (t.equals("Y")) k = 1;      // 1:1
        else if (t.equals("F")) k = 2; // 2:2
        else k = 3;                    // 3:3 (O)

        Set<String> unique = new HashSet<>();
        for (int i = 0; i < n; i++) unique.add(br.readLine());

        System.out.println(unique.size() / k);
    }
}
