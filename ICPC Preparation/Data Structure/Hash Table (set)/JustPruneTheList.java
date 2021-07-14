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
			HashMap<Integer, Integer> hashA = new HashMap<>();
			HashMap<Integer, Integer> hashB = new HashMap<>();
			TreeSet<Integer> treeSet = new TreeSet<>();

			int aws = 0;
			for (int i = 0; i < n; i++) {
				int aux = fs.nextInt();
				treeSet.add(aux);
				if (hashA.containsKey(aux)){
					int hash = hashA.get(aux);
					hash++;
					hashA.put(aux, hash);
				}else{
					hashA.put(aux, 1);
				}
			}
			for (int i = 0; i < m; i++) {
				int aux = fs.nextInt();
				treeSet.add(aux);
				if (hashB.containsKey(aux)){
					int hash = hashB.get(aux);
					hash++;
					hashB.put(aux, hash);
				}else{
					hashB.put(aux, 1);
				}
			}
			for (int d:treeSet) {
				if (hashA.containsKey(d) && !hashB.containsKey(d)){
					aws+= hashA.get(d);
				}else if (!hashA.containsKey(d) && hashB.containsKey(d)){
					aws+= hashB.get(d);
				}else{
					aws+= Math.abs(hashA.get(d)-hashB.get(d));
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
