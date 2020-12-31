import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12250 - Language Detection
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3402
public class LanguageDetection {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int n=0;
        while (true){
            String word = fs.next();
            if (word.equals("#"))break;
            n++;
            switch (word){
                case "HELLO":
                    System.out.println("Case " +n+": ENGLISH");
                    break;
                case "HOLA":
                    System.out.println("Case " +n+": SPANISH");
                    break;
                case "HALLO":
                    System.out.println("Case " +n+": GERMAN");
                    break;
                case "BONJOUR":
                    System.out.println("Case " +n+": FRENCH");
                    break;
                case "CIAO":
                    System.out.println("Case " +n+": ITALIAN");
                    break;
                case "ZDRAVSTVUJTE":
                    System.out.println("Case " +n+": RUSSIAN");
                    break;
                default:
                    System.out.println("Case " +n+": UNKNOWN");
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
