import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 10424 - Love Calculator
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1365
public class LoveCalculator {
    static int recurseSum (int i) {
        if (i<10) {
            return i;
        } else {
            int sum=0;
            while (i>0) {
                sum+=i%10;
                i/=10;
            }
            return recurseSum(sum);
        }
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()){
            int sum=0,sum2=0;
            char[] arr1 = sc.next().toCharArray();sc.nextLine();
            char[] arr2 = sc.next().toCharArray();
            for (char data : arr1) {
                if (Character.isAlphabetic(data)){
                    if (Character.isUpperCase(data)) {
                        sum+=(data-'A'+1);
                    } else {
                        sum+=(data-'a'+1);
                    }
                }
            }
            for (char data : arr2) {
                if (Character.isAlphabetic(data)){
                    if (Character.isUpperCase(data)) {
                        sum2+=(data-'A'+1);
                    } else {
                        sum2+=(data-'a'+1);
                    }
                }
            }
            sum=recurseSum(sum);
            sum2=recurseSum(sum2);
            System.out.printf("%.2f %%\n", (double)((Math.min((double) sum,(double) sum2)/Math.max((double) sum,(double) sum2)*100)));

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
