import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12545 - Bits Equalizer
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3990
public class BitsEqualizer {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        int test = 0;
        while (t!=0){
            test++;
            char[] str = fs.next().toCharArray();
            char[] str2 = fs.next().toCharArray();
            int aws0=0, aws1=0;
            int awsS1=0,awsS2=0;
            for (int i = 0; i < str.length; i++) {
                if (str[i]=='0' && str2[i]=='1') aws0++;
                if (str[i]=='1' && str2[i]=='0') aws1++;
                if (str[i]=='?'){
                    if (str2[i]=='1') awsS1++;
                    awsS2++;
                }
            }
            if (aws1>aws0+awsS1) System.out.println("Case "+test+": "+"-1");
            else System.out.println("Case "+test+": "+(Math.max(aws0,aws1)+awsS2));

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
