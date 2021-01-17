import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class C {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        int[] math = new int[105];
        while (t != 0) {
            int n = fs.nextInt();
            int[] arr = fs.readArray(n);
            Arrays.sort(arr);
            int ans = 0;
            for (int i = 2; i <= 2 * n; i++) {
                int cnt = 0;
                int l = 1;
                int r = n;
                while (l < r) {
                    if (arr[l] + arr[r] == i) {
                        l++;
                        r--;
                        cnt++;
                    } else if (arr[l] + arr[r] < i) {
                        l++;
                    } else r--;
                }
                ans = Math.max(ans, cnt);
            }
            System.out.println(ans);
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
            int[] a = new int[n + 1];
            for (int i = 1; i <= n; i++) a[i] = nextInt();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
