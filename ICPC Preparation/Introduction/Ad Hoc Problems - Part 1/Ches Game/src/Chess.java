import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Chess {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t != 0) {
            char data = fs.next().charAt(0);
            int n = fs.nextInt();
            int m = fs.nextInt();
            switch (data) {
                case 'r':
                    System.out.println(Math.min(n, m));
                    break;
                case 'Q':
                    System.out.println(Math.min(n, m));
                    break;
                case 'k':
                    System.out.println(((n * m) + 1) / 2);
                    break;
                case 'K':
                    System.out.println(((n + 1) / 2) * ((m + 1) / 2));
                    break;
            }
            t--;
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
