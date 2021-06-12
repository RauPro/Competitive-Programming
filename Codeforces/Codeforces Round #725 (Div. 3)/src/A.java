import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		while (t -->0){
			int n = fs.nextInt();
			int[] arr = fs.readArray(n);
			int maxPower = Arrays.stream(arr).max().getAsInt();
			int minPower = Arrays.stream(arr).min().getAsInt();
			int minIndex = 0;
			int maxIndex = 0;
			int awsNormal = 0;
			int ans = 0;
			int ansBack =0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i]==minPower){
                    minIndex = i;
                }
                if (arr[i]==maxPower){
                    maxIndex = i;
                }
            }
            int min =  Math.min(minIndex, maxIndex);
            int max = Math.max(minIndex,maxIndex);
            for (int i = 0; i < arr.length; i++) {
                if (arr[i]==maxPower || arr[i]==minPower){
                    awsNormal++;
                }
                if (awsNormal==2){
                    ans=i+1;
                    awsNormal = 0;
                    break;
                }
            }
            int custom = 0;
            for (int i = arr.length-1; i >= 0; i--) {
                if (arr[i]==maxPower || arr[i]==minPower){
                    awsNormal++;
                }
                if (awsNormal==2){
                    ansBack = custom+1;
                    break;
                }
                custom++;
            }
            System.out.println(Math.min((n-max)+min+1, Math.min(ans, ansBack)));
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
