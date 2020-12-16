import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class C {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t= fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            if (n>45){
                System.out.println("-1");
                t--;
                continue;
            }
            ArrayList<Integer> arr  = new ArrayList<>();
            int sum=0,ar=9;
            while (sum+ar<n){
                sum+=ar;
                arr.add(ar);
                ar--;
            }
            if (sum!=n){
                arr.add(n-sum);
            }
            Collections.reverse(arr);
            for (int data:arr) {
                System.out.print(data);
            }
            System.out.println("");
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
