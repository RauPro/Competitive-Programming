import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// UVa 12247 - Jollo
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3399
public class Jollo {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true) {
            boolean[] avalible = new boolean[54];
            int[] princess = fs.readArray(3);
            int[] prince = fs.readArray(2);

            if (princess[0] + princess[1] + princess[2] + prince[0] + prince[1] == 0) {
                break;
            }
            Arrays.fill(avalible, true);
            for (int i = 0; i < 3; ++i) {
                avalible[princess[i]] = false;

                if (i < 2)
                    avalible[prince[i]] = false;
            }
            Arrays.sort(prince);
            Arrays.sort(princess);
            int card = 53;
            if (prince[0] > princess[2]) {
                for (int i = 1; i <= 52 && i < card; ++i)
                    if (avalible[i])
                        card = i;
            }
            if (prince[1] > princess[2]) {
                for (int i = princess[2] + 1; i <= 52 && i < card; ++i) {

                    if (avalible[i])
                        card = i;
                }
            }
            if (prince[0] > princess[1]) {
                for (int i = princess[1] + 1; i <= 52 && i < card; ++i)
                    if (avalible[i])
                        card = i;
            }

            if (card == 53)
                card = -1;
            System.out.println(card);
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
