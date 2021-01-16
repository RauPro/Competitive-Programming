import javafx.scene.control.Alert;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class CardsExchange {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        while (true){
            int n = fs.nextInt();
            int m = fs.nextInt();
            if (n ==0 && m==0)break;
            int[] Alice = new int[n];
            int[] Betty = new int[m];
            int[] awsA = new int[100000];
            int[] awsB = new int[100000];
            int currentValue = 0;
            int aws = 0;
            int aws2 = 0;
            for (int i = 0; i < n; i++) {
                currentValue=fs.nextInt();
                if (i>0 && currentValue!=Alice[i-1]){
                    Alice[i]=currentValue;
                    awsA[Alice[i]]++;
                    continue;
                }
                if (i==0){
                    Alice[i]=currentValue;
                    awsA[Alice[i]]++;
                    continue;
                }
                i--;
                n--;
            }
            for (int i = 0; i < m; i++) {
                currentValue=fs.nextInt();
                if (i>0 && currentValue!=Betty[i-1]){
                    Betty[i]=currentValue;
                    awsB[Betty[i]]++;
                    continue;
                }
                if (i==0){
                    Betty[i]=currentValue;
                    awsB[Betty[i]]++;
                    continue;
                }
                i--;
                m--;
            }
            /*for (int data:Betty) {
                System.out.print(data+" ");
            }
            System.out.println();
            for (int data:Alice) {
                System.out.print(data+" ");
            }
            System.out.println();*/
            for (int i = 0; i < n; i++) {
                if (awsB[Alice[i]]==0){
                    //System.out.println(Alice[i]);
                    aws++;
                }
            }
            //System.out.println();
            for (int i = 0; i < m; i++) {
                if (awsA[Betty[i]]==0){
                    //System.out.println(Betty[i]);
                    aws2++;
                }
            }
            //System.out.println();
            System.out.println(Math.min(aws2,aws));
            //System.out.println();

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
