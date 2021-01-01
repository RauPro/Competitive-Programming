import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12279 - Emoogle Balance
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3431
public class EmoogleBalance {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int testCase = 0;
        while (true){
            testCase++;
            int n = fs.nextInt();
            if (n==0)break;
            int awsP=0;
            int[] arr = fs.readArray(n);
            for (int data:arr) {
                if (data>0)awsP++;
            }
            int aws = awsP-(n-awsP);
            System.out.println("Case "+testCase+": "+aws);
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
