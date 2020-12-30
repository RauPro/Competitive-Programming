import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 12150 - Pole Position
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3302
public class PolePosition {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        test: while (true){
            int n = sc.nextInt();
            if (n==0)break;
            int[] cars = new int[n];
            int[] position = new int[n];
            ArrayList<Integer> list = new ArrayList<>();
            Collections.fill(list,0);
            for (int i = 0; i < n; i++) {
                cars[i]= sc.nextInt();
                list.add(cars[i]);
                position[i] = sc.nextInt();
            }
            int sum=Integer.MAX_VALUE;
            try {
                for (int i = 0; i < n; i++) {
                    int caseTest = position[i];
                    if (sum==i+caseTest){
                        System.out.println("-1");
                        continue test;
                    }
                    //System.out.println(cars[i]);
                    sum= i+caseTest;
                    list.set(i+caseTest,cars[i]);
                }
            }catch (Exception e){
                System.out.println("-1");
                continue test;
            }
            for (int data:list) {
                System.out.print(data+" ");
            }
            System.out.println();
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
