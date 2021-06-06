import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t  = fs.nextInt();
		while (t!=0){
		    int n = fs.nextInt();
			int[] arr = fs.readArray(n);
			int aws = 0;
			ArrayList<Integer> aux = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (arr[i]%2==0){
                    aux.add(arr[i]);
                }
            }
            for (int i = 0; i < n; i++) {
                if (arr[i]%2==1){
                    aux.add(arr[i]);
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = i+1; j < n; j++) {
                    if (gcdThing(aux.get(i), 2*aux.get(j))>1){
                        aws++;
                    }
                }
            }
            System.out.println(aws);
			t--;
		}
    }
    static int gcdThing(int a, int b) {
        BigInteger b1 = BigInteger.valueOf(a);
        BigInteger b2 = BigInteger.valueOf(b);
        BigInteger gcd = b1.gcd(b2);
        return gcd.intValue();
    }
    static int gcd(int a, int b){
        while(b>0){
            int r= a%b;
            a = b;
            b = r;
        }
        return a;
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
