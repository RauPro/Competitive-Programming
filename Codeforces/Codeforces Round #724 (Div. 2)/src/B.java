import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        while (t != 0) {
            int n = fs.nextInt();
            String s = fs.next();
            ArrayList<String> arr = new ArrayList<>();
            arr.add("");
            for (int i = 0; i < arr.size(); i++) {
                String c = arr.get(i);
                if (!s.contains(c)) {
                    System.out.println(c);
                    break;
                }
                for (char d:alphabet){
                    arr.add(c + d);
                }
            }
            t--;
        }
    }
    /*static String makeSrt(StringBuilder st, char[] alphabet){
        StringBuilder srt = new StringBuilder();
        for (int i = 0; i < alphabet.length; i++) {
            for (int j = 0; j < alphabet.length; j++) {
                srt.append(alphabet[i]);
                if (srt.toString().compareTo(st.toString())>0){
                    return srt.toString();
                }
                srt.append(alphabet[j]);
                if (srt.toString().compareTo(st.toString())>0){
                    return srt.toString();
                }

            }
        }
    }*/
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
