import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class A {
    static int findBeauty(int arr[],int n,float x) {
        double res=0;
        for(int i=0;i<n;i++) {
            double add= Math.ceil((float) (arr[i]/x));
            res=res+add;
        }
        return (int)res;
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int n,x;
            n= fs.nextInt();
            x = fs.nextInt();

            int[] arr = fs.readArray(n);
            double beauty1 = findBeauty(arr,n,x);
            float cnt=0;

            for(int i=0;i<n;i++)
            {
                cnt=cnt+arr[i];
            }
            double beauty2=Math.ceil (cnt/x);

            if(beauty1>beauty2){
                System.out.println((int)beauty2+" "+(int)beauty1);
            } else {
                System.out.println((int)beauty1+" "+(int)beauty2);
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
