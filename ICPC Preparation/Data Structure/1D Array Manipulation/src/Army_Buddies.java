import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12356 - Army Buddies
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3778
public class Army_Buddies {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true){
            int solders = fs.nextInt();
            int kills = fs.nextInt();
            if (solders==0 && kills==0)break;
            int[] right = new int[Integer.MAX_VALUE/200];
            int[] left = new int[Integer.MAX_VALUE/200];
            for (int i = 0; i < solders+1; i++) {
                left[i]=i-1;
                right[i]=i+1;
            }
            for (int i = 0; i < kills; i++) {
                int a = fs.nextInt();
                int b=fs.nextInt();
                if (left[a]<1) System.out.print("* ");
                else System.out.print(left[a]+" ");

                if (right[b]>solders) System.out.println("* ");
                else System.out.println(right[b]);

                left[right[b]]=left[a];
                right[left[a]]=right[b];
            }
            System.out.println("-");


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
