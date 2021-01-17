import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t != 0) {
            int n = fs.nextInt();
            int[] arr1 = fs.readArray(n);
            int[] arr2 = fs.readArray(n);
            int minA = Arrays.stream(arr1).min().getAsInt();
            int minB =Arrays.stream(arr2).min().getAsInt();
            int MaxMin = Math.max(minA,minB);
            long aws = 0;
            for (int i = 0; i < n; i++) {
                if (arr1[i]>minA && arr2[i]>minB){
                    int data1 =arr1[i]-minA;
                    int data2 =arr2[i]-minB;
                    int ans =Math.min(data1,data2);
                    aws+=ans;
                    arr1[i]-=ans;
                    arr2[i]-=ans;
                }
                if (arr1[i]>minA){
                    aws+=Math.abs(arr1[i]-minA);
                    arr1[i]=arr1[i]-minA;
                }
                if (arr2[i]>minB){
                    aws+=Math.abs(arr2[i]-minB);
                    arr2[i]=arr2[i]-minB;
                }
                //  System.out.println(aws);
            }
            System.out.println(aws);
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
