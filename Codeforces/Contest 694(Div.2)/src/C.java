import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class C {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        long[] pos=new long[300005];
        long[] presents=new long[300005];
        int t = fs.nextInt();
        while (t!=0){
            long sum = 0;
            int n = fs.nextInt();
            int m=fs.nextInt();
            Arrays.fill(pos,0);
            for (int i = 1; i <= n; i++) {
                int x=fs.nextInt();
                pos[i]++;
                pos[x]++;
            }
            for (int i = 1; i <= m; i++) presents[i]=fs.nextInt();
            int index = 1;
            while (n>0) {
                if (n >= pos[index]) {
                    sum += (presents[index] * pos[index]);
                    n -= pos[index];
                }
                else {
                    sum += (presents[index] * n);
                    n = 0;
                }
                index++;
            }
            System.out.println(sum);
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
