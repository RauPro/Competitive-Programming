import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            int[] arr = new int[n];
            arr = fs.readArray(n);
            int[] aux = new int[n];
            int aws=0;
            for (int i = 0; i < n; i++) {
                    try {
                        aux[aws]=arr[i];
                        aws+=2;
                    }catch (ArrayIndexOutOfBoundsException e){
                        continue;
                    }
            }
            int coms=1;
            for (int i = arr.length-1; i >=1 ; i--) {
                try {
                    aux[coms]=arr[i];
                    coms+=2;
                }catch (ArrayIndexOutOfBoundsException e){
                    continue;
                }
            }for (int data:aux) {
                System.out.print(data + " ");
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
