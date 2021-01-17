import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class D {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t != 0) {
            int n = fs.nextInt();
            char[] s = fs.next().toCharArray();
            int[] ans = new int[n];
            ArrayList<Integer> pos0 = new ArrayList<>();
            ArrayList<Integer> pos1 = new ArrayList<>();
            for (int i = 0; i < n; ++i) {
                int newpos = pos0.size() + pos1.size();
                if (s[i] == '0') {
                    if (pos1.isEmpty()) {
                        pos0.add(newpos);
                    } else {
                        newpos = pos1.get(pos1.size()-1);
                        pos1.remove(pos1.size()-1);
                        pos0.add(newpos);
                    }
                } else {
                    if (pos0.isEmpty()) {
                        pos1.add(newpos);
                    } else {
                        newpos = pos0.get(pos0.size()-1);
                        pos0.remove(pos0.size()-1);
                        pos1.add(newpos);
                    }
                }
                ans[i] = newpos;
            }
            System.out.println(pos0.size() + pos1.size());
            for (int data:ans) {
                System.out.print(data+1+" ");
            }
            System.out.println();            t--;
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
