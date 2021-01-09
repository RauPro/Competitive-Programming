import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 11786 - Global Raining at Bididibus
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2886
public class GlobalRainingatBididibus {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int aws = 0;
            Stack<Integer> characterStack = new Stack<>();
            char[] arr = fs.next().toCharArray();
            for (int i = 0; i < arr.length; i++) {
                if (arr[i]=='\\'){
                    characterStack.push(i);
                }else if (arr[i]=='/' && !characterStack.empty()){
                    aws+=i-characterStack.pop();
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
