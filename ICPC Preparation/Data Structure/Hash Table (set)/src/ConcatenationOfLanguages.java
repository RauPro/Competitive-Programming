import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class ConcatenationOfLanguages {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int cases = 1;
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();;
        while (t!=0){
            int m = sc.nextInt();
            int n = sc.nextInt();sc.nextLine();
            ArrayList<String> setA = new ArrayList<>();
            ArrayList<String> setB = new ArrayList<>();
            TreeSet<String> aws = new TreeSet<>();
            for (int i = 0; i < m; i++) {
                String aux = sc.nextLine();
                setA.add(aux);
            }
            for (int i = 0; i < n; i++) {
                String aux = sc.nextLine();
                setB.add(aux);
            }
            for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        aws.add(setA.get(i)+setB.get(j));
                    }
            }
            System.out.println("Case "+cases+": "+aws.size());
            cases++;

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
