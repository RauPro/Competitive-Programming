import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 1709 - Amalgamated Artichokes
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4782
public class AmalgamatedArtichokes {
    static double stock(int[] arr){
        double aws=0.00;
        double ret = Double.MIN_VALUE;
        for (int i = 1; i <= arr[5]; i++) {
            double ans = arr[0]*(Math.sin(arr[1]*i+arr[2])+Math.cos(arr[3]*i+arr[4])+2);
            aws=Math.max(aws,ret-ans);
            ret = Math.max(ret,ans);

        }
        return aws;
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()){
            int[] arr = new int[6];
            for (int i = 0; i < 6; i++) {
                arr[i]=sc.nextInt();
            }
            System.out.println(stock(arr));
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
