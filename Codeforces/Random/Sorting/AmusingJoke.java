import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class AmusingJoke {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        char[] arr1 = fs.next().toCharArray();
        char[] arr2 = fs.next().toCharArray();
        char[] aws = fs.next().toCharArray();
        char[] result = new char[arr1.length+arr2.length];
        int[] acum = new int[500];
        int[] acumAws = new int[500];
        System.arraycopy(arr1, 0, result, 0, arr1.length);
        System.arraycopy(arr2, 0, result, arr1.length, arr2.length);
        if (result.length!=aws.length){
            System.out.println("NO");
            return;
        }
        for (char data:result) {
            acum[data]++;
        }
        for (char data:aws) {
            acumAws[data]++;
        }
        int self=0;
        for (char data:aws) {
            if (acum[data]!=acumAws[data]){
                self++;
                break;
            }
        }

        System.out.println(self==0?"YES":"NO");
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
