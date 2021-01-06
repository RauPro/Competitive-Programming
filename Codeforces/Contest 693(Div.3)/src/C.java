import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class C {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            long[] a = fs.readLongArr(n);
            long aws = Long.MIN_VALUE;
            long[] s = new long[n];
            for (int i = 0; i < n; i++) {
                if (a[i] > s[i]) {
                    s[i] = a[i];
                    aws = Math.max(a[i], aws);
                }
                if (i + a[i] < n) {
                    s[(int) (i + a[i])] = Math.max(s[(int) (i + a[i])], s[i] + a[(int) (i + a[i])]);
                    aws = Math.max(s[(int) (i + a[i])], aws);
                }
            }

            System.out.println(aws);
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
        long[] readLongArr(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = nextLong();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
