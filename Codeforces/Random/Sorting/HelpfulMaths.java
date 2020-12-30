import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class HelpfulMaths {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        char[] arr = fs.next().toCharArray();
        List<Character> sorted = new ArrayList<>();
        for (int i = 0; i < arr.length; i+=2) {
            sorted.add(arr[i]);
        }Collections.sort(sorted);
        if (sorted.size()==1){
            System.out.println(sorted.get(0));
        }else {
            for (int i=0;i<sorted.size();i++) {
                if (i==sorted.size()-1){
                    System.out.print(sorted.get(i));
                }else {
                    System.out.print(sorted.get(i)+"+");
                }
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
