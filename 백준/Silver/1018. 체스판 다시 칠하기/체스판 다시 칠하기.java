import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static StringTokenizer tokens;
    static int n, m;
    static char[][] map;
    static int min = Integer.MAX_VALUE;
    static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        tokens = new StringTokenizer(input.readLine());
        m = Integer.parseInt(tokens.nextToken());
        n = Integer.parseInt(tokens.nextToken());
        map = new char[m][n];
        
        for (int i = 0; i < m; i++) {
            String str = input.readLine();
            for (int j = 0; j < n; j++) {
                map[i][j] = str.charAt(j);
            }
        }

        // Check every 8x8 section
        for (int i = 0; i <= m - 8; i++) {
            for (int j = 0; j <= n - 8; j++) {
                min = Math.min(min, repaintCost(i, j));
            }
        }
        
        System.out.println(min);
    }

    // Calculate repaint cost for 8x8 starting at (startX, startY)
    static int repaintCost(int startX, int startY) {
        int repaintW = 0; // Cost if top-left corner is 'W'
        int repaintB = 0; // Cost if top-left corner is 'B'

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                // Determine what the correct color should be
                char expectedColor = ((i + j) % 2 == 0) ? 'W' : 'B';
                char altColor = ((i + j) % 2 == 0) ? 'B' : 'W';
                
                if (map[startX + i][startY + j] != expectedColor) repaintW++;
                if (map[startX + i][startY + j] != altColor) repaintB++;
            }
        }

        // Return the minimum repaint cost of the two patterns
        return Math.min(repaintW, repaintB);
    }
}