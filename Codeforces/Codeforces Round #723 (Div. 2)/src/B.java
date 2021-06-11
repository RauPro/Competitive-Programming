import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		Boolean[] dp = new Boolean[2000];
		dp[0] = true;
		for (int i = 1; i < 2000; i++) {
			dp[i] = (i >= 11 && dp[i - 11]) || (i >= 111 && dp[i - 111]) || (i >= 1111 && dp[i - 1111]);
		}
		while (t-- > 0){
			int n = fs.nextInt();
			if (n>dp.length){
				System.out.println("YES");
				continue;
			}
			System.out.println(dp[n]? "YES": "NO");
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
