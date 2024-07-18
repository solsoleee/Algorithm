import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {
    private static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder output = new StringBuilder();
    private static StringTokenizer tokens;

    public static void main(String[] args) throws NumberFormatException, IOException {
        int n = Integer.parseInt(input.readLine());
        List<BigInteger> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            tokens = new StringTokenizer(input.readLine());
            String pre = "";
            Boolean flag = false; // 이전에 문자가 있었는지 여부
            String str = tokens.nextToken();
            for (int j = 0; j < str.length(); j++) {
                if (Character.isDigit(str.charAt(j))) {
                    flag = true;
                    pre = pre + str.charAt(j);
                } else {
                    if (flag) {
                        list.add(new BigInteger(pre));
                        pre = "";
                        flag = false;
                    }
                }
            }
            if (flag) {
                list.add(new BigInteger(pre));
            }
        }

        Collections.sort(list);
        for (BigInteger r : list) {
            System.out.println(r);
        }
    }
}