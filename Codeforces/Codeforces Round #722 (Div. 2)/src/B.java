import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		while (t-->0){
			int n = fs.nextInt();
			int[] arr = fs.readArray(n);
			int aws = 1;
			int inf = Integer.MAX_VALUE;
			Arrays.sort(arr);
            for (int i = 1; i < n; i++) {
                inf = Math.min(inf,Math.abs( arr[i]-arr[i-1]));
                if (inf<arr[i]){
                    break;
                }
                aws++;
            }
			System.out.println(aws);
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
