import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 11559 - Event Planning
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2595
public class EventPlanning {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()){
            boolean flag = false;
            int n = sc.nextInt();
            int b = sc.nextInt();
            int h = sc.nextInt();
            int w = sc.nextInt();
            int auaxDatum = Integer.MAX_VALUE;
            while (h!=0){
                int p= sc.nextInt();
                int[] wArray = new int[w];
                for (int i = 0; i < w; i++) {
                    wArray[i]=sc.nextInt();
                    if (wArray[i]>=n){
                        if (wArray[i]*p<=b){
                            flag=true;
                            auaxDatum=Math.min(auaxDatum,n*p);
                        }
                    }
                }
                h--;
            }
            System.out.println(flag?auaxDatum:"stay home");
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
