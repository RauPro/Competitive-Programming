import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12372 - Packing for Holiday
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=0&problem=3794
public class PackingforHoliday {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs .nextInt();
        int n =0;
        while (t!=0){
            n++;
            int [] arr = fs.readArray(3);
            if (arr[1]<=20 && arr[2]<=20 && arr[0]<=20) System.out.println("Case "+n+": good");
            else System.out.println("Case "+n+": bad");
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
