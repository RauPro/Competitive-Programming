import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 11764 - Jumping Mario
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2864
public class JumpingMario {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t= fs.nextInt();
        int caseTest=0;
        while (t!=0){
            caseTest++;
            int n =fs.nextInt();
            int[] arr = fs.readArray(n);
            int awsLow=0;
            int awsHig=0;
            for (int i = 0; i < n-1; i++) {
                if ((arr[i]<arr[i+1])){
                    awsLow++;
                }else if (arr[i]!=arr[i+1]) awsHig++;
            }
            System.out.println("Case "+caseTest+": "+awsLow+" "+awsHig);
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
