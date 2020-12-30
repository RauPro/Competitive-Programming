import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// UVa 10038 - Jolly Jumpers
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=979
public class JollyJumpers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        FastScanner fs =new FastScanner();
        while (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            if (n == 1) {
                System.out.println("Jolly");
                continue;
            }
            boolean[] nums = new boolean[n - 1];
            for (int i = 0; i < n - 1; i++) {
                int set = Math.abs(arr[i] - arr[i + 1]) - 1;//For the index
                if (0 <= set && set < nums.length) nums[set] = true;
            }
            boolean valid = true;
            for (boolean b : nums) {
                valid = valid && b;
            }
            System.out.println(valid ? "Jolly" : "Not jolly");
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
