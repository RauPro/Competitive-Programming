import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t= fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            int size, awsOne = 0, awsTwo = 0;
            for (int i=0;i<n;i++) {
                size = fs.nextInt();
                if (size==1) awsOne += 1;
                else awsTwo += 1;
            }
            if (awsTwo%2!=0) {
                if (awsOne>1) {
                    awsOne -= 2;
                    awsTwo += 1;
                }
            }
            if (awsOne%2==0 && awsTwo%2==0) System.out.println("YES");
            else System.out.println("NO");
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
