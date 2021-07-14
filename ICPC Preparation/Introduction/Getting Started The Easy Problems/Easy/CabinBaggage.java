import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 12696 - Cabin Baggage

public class CabinBaggage {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        int aws = 0;
        while (t!=0){
            double l = 56.00,w=45.00,d=25.00;
            double[] arr = new double[4];
            for (int i = 0; i < 4; i++) {
                arr[i]=fs.nextDouble();
            }
            double sumArr = Arrays.stream(arr).sum()-arr[3];
            int flag = 1;
            if(arr[3]<=7.00){
                if(arr[0]<=56 && arr[1] <=45 && arr[2]<=25)
                {
                    flag=1;
                }
                else if(sumArr<=125 )
                {
                    flag=1;
                }
                else
                    flag=0;
            }
            else{
                flag=0;
            }
            System.out.println(flag);
            aws+=flag;
            t--;
        }
        System.out.println(aws);
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
        double nextDouble() {
            return Double.parseDouble(next());
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
