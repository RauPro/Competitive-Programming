import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class WhastheCard {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int test=0;
        int t = fs.nextInt();
        while (t!=0){
            String[] arr = new String[52];
            test++;
            for (int i = 0; i < 52; i++) {
                arr[i]=fs.next();
            }
            System.out.println("Case "+test+": "+arr[32]);
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
