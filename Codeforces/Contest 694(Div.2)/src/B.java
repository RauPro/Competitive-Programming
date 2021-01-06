import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Inet4Address;
import java.util.*;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            int x = fs.nextInt();
            int sum=0;
            ArrayList<Integer> list = new ArrayList<>();

            for (int i = 0; i < n; i++) {
                int data = fs.nextInt();
                list.add(data);
                sum+=data;
            }
            int i = 0;
            int k = x;
            int count = 0;
            while (true) {
                if (list.get(i) % x != 0) break;
                if (count == n) {
                    k *= x;
                    count = 0;
                }
                list.add((list.get(i) / x));
                sum += k * (list.get(i) / x);
                i++;
                count++;
            }

            System.out.println(sum);
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
