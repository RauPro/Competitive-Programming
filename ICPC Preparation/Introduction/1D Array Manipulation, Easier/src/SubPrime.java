import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 11679 - Sub-prime
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2726
public class SubPrime {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true){
            int b = fs.nextInt();
            int n= fs.nextInt();
            if (b == 0 && n == 0){
                break;
            }
            else {
                int[] arr = new int[100];
                for (int i = 0; i < b; i++) {
                    arr[i]= fs.nextInt();
                }
                for (int i = 0; i < n; i++) {
                    int a = fs.nextInt();
                    int d = fs.nextInt();
                    int amount = fs.nextInt();
                    arr[a-1]-=amount;
                    arr[d-1]+=amount;
                }
                boolean isPossible = true;
                for (int i = 0; i < b; i++) {
                    if (arr[i]<0){
                        isPossible=false;
                    }
                }
                System.out.println(isPossible?"S":"N");
            }

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
