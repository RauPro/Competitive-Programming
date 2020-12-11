import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t= fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            int k = fs.nextInt();

            char[] letter = new char[]{'a','b','c'};
            ArrayList<Character> listA = new ArrayList<>();
            while (n!=0){
                for (int i = 0; i < 3; i++) {
                    for (int j=0;j<k;j++){
                        listA.add(letter[i]);
                        n--;
                        if (n==0){
                            break;
                        }
                    }
                    if (n==0){
                        break;
                    }
                }
            }
            for (char c : listA){
                System.out.print(c);
            }
            System.out.print("\n");
            t--;
        }

    }
    static class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
        int[] readArray(int n) {
            int[] a=new int[n];
            for (int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
