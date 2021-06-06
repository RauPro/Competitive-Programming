import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t  = fs.nextInt();
        while (t!=0){
            int[] arr = fs.readArray(4);
            int maxLvlA = Math.max(arr[0], arr[1]);
            int maxLvlB = Math.max(arr[2], arr[3]);
            int aws = 0;
            for (int i = 0; i < 2; i++) {
                if (maxLvlB<arr[i]){
                    aws++;
                }
            }
            for (int i = 2; i < 4; i++) {
                if (maxLvlA<arr[i]){
                    aws++;
                }
            }
            System.out.println(aws!=2?"YES":"NO");
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
