import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class CD {
	public static void main(String[] args) {
		FastScanner fs = new FastScanner();
		while (true){
			int n = fs.nextInt();
			int m = fs.nextInt();
			if (n==0 && m==0){
				break;
			}
			TreeSet<Integer> setDisk = new TreeSet<>();
			for (int i = 0; i < n; i++) {
				int aux = fs.nextInt();
				setDisk.add(aux);
			}
			int aws = 0;
			for (int i = 0; i < m; i++) {
				int aux = fs.nextInt();
				if (setDisk.contains(aux)){
					aws++;
				}
			}
			System.out.println(aws);
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
