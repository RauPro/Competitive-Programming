import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class AGiveaway {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		while (true){
			int n = fs.nextInt();
			if (n==0){
			    break;
            }
            TreeSet<Integer> treeSetSqrt = new TreeSet<>();
            TreeSet<Integer> treeSetExp = new TreeSet<>();
            for (int i = 1; i <= n; i++) {
                int aux = (int)Math.pow(i,2);
                treeSetSqrt.add(aux);
                if (aux>=n){
                    break;
                }
            }
            for (int i = 1; i <= n; i++) {
                int aux = (int)Math.pow(i,3);
                treeSetExp.add(aux);
                if (aux>=n){
                    break;
                }
            }
            if (treeSetExp.contains(n) && treeSetSqrt.contains(n)){
                System.out.println("Special");
            }else{
                System.out.println("Ordinary");
            }
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
