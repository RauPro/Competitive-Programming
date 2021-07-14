import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class HowManyKnights {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true) {
            int n = fs.nextInt();
            int m = fs.nextInt();
            if (m == 0 && n == 0) {
                break;
            }
            int ans = 0, k = 0;
            if (m == 1 || n == 1)
                ans = m * n;
            else if (m == 2 || n == 2) {
                if (m == 2)
                    k = n;
                else
                    k = m;
                int c = (k % 4 == 0) ? k / 4 : (k / 4) + 1;
                int d = ((k - 1) % 4 == 0) ? (k - 1) / 4 : ((k - 1) / 4) + 1;
                ans = 2 * (c + d);
            } else
                ans = ((m * n) % 2 == 0) ? (m * n) / 2 : ((m * n) / 2) + 1;
            System.out.println(ans + " knights may be placed on a " + n + " row " + m + " column board.");
        }
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens())
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
