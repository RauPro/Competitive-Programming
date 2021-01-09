import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12015 - Google is Feeling Lucky
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3166
public class GoogleisFeelingLucky {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t=fs.nextInt();
        int testCase=0;
        while (t != 0) {
            testCase++;
            int maxNum=0;
            ArrayList<String> site = new ArrayList<>();
            ArrayList<Integer> feels = new ArrayList<>();
            for (int i = 0; i < 10; i++) {
                String st = fs.next();
                int tn = fs.nextInt();
                site.add(st);
                feels.add(tn);
                maxNum= Math.max(maxNum,tn);
            }
            System.out.println("Case #"+testCase+":");
            for (int i = 0; i < 10; i++) {
                if (feels.get(i)==maxNum){
                    System.out.println(site.get(i));
                }
            }
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
