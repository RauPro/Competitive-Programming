import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 11687 - Digits
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2734
public class Digits {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true){
            StringBuilder sb = new StringBuilder();
            String str = fs.next();
            if (str.equals("END"))break;
            int lenght = str.length();
            if (str.equals("1")) {
                sb.append(1);
            } else if (lenght < 2) {
                sb.append(2);
            } else if (lenght < 10) {
                sb.append(3);
            } else {
                sb.append(4);
            }
            System.out.println(sb);
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
