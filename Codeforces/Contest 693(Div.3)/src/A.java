import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int aws= 1;
            int[] arr = fs.readArray(3);
            while ((arr[0]%2)==0 || (arr[1]%2)==0) {
                if (aws==arr[2]) break;
                if (arr[0]%2==0) {
                    aws *= 2;
                    arr[0] = arr[0]/2;
                }
                else if (arr[1]%2==0) {
                    aws *= 2;
                    arr[1] = arr[1]/2;
                }
            }
            if (aws>=arr[2]) {
                System.out.println("YES");
            } else System.out.println("NO");
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
