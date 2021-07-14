import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class TariffPlan {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        int testCase = 0;
        while (t!=0){
            testCase++;
            int n = fs.nextInt();
            int[] arr = fs.readArray(n);
            int mileCost = 0;
            int juiceCost = 0;
            for (int i = 0; i < arr.length; i++) {
                mileCost+=((arr[i]/30)+1)*10;
                juiceCost+=((arr[i]/60)+1)*15;
            }
            if (mileCost<juiceCost) {
                System.out.println("Case "+testCase+": Mile "+mileCost);
            } else if (juiceCost<mileCost) {
                System.out.println("Case "+testCase+": Juice "+juiceCost);
            } else {
                System.out.println("Case "+testCase+": Mile Juice "+mileCost);
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
