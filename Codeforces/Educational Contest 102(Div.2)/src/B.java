import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B {
    static int gcd(int a, int b){
        if(b == 0) return a;
        return gcd(b,a%b);
    }

    static int lcm(int a, int b){
        int g = gcd(a,b);
        a = a/g;
        b = b/g;
        return a*b*g;
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t != 0) {
            String s=fs.next();
            String k=fs.next();
            long l = lcm(s.length(),k.length());
            StringBuilder left = new StringBuilder();
            StringBuilder right = new StringBuilder();
            for(int i = 0 ; i < l/s.length() ; i++){
                left.append(s);
            }
            for(int i = 0 ; i < l/k.length() ; i++){
                right.append(k);
            }

            if(left.toString().equals(right.toString())) System.out.println(left);
            else System.out.println(-1);
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
