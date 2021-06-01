import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class JustPruneTheList {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		while (t!=0){
			int n = fs.nextInt();
			int m = fs.nextInt();
			int[] hashA = new int[10000+1];
			int[] hashANegative = new int[10000+1];
			int[] hashB = new int[10000+1];
			int[] hashBNegative = new int[10000+1];

			int aws = 0;
			for (int i = 0; i < n; i++) {
				int aux = fs.nextInt();
				if (aux>=0){
					hashA[aux]++;
				}
				else{
					hashANegative[Math.abs(aux)]++;
				}
			}
			for (int i = 0; i < m; i++) {
				int aux = fs.nextInt();
				if (aux>=0){
					hashB[aux]++;
				}
				else{
					hashBNegative[Math.abs(aux)]++;
				}
			}
			for (int i = 0; i < hashA.length; i++) {
				if (hashA[i]!=hashB[i]){
					aws+=Math.abs(hashA[i]-hashB[i]);
				}
				if (hashANegative[i]!=hashBNegative[i]){
					aws+=Math.abs(hashANegative[i]-hashBNegative[i]);
				}
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
