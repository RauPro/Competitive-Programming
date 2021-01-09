import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 1585 - Score
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4460
public class Score {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            char[] arr = fs.next().toCharArray();
            int [] ans = new int[arr.length];
            int aws = 0;
            int aux = 0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i]=='O'){
                    aws++;
                    ans[i]=aws;
                }else {
                    aux+=aws;
                    aws=0;
                }
            }
            System.out.println(Arrays.stream(ans).sum());
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
