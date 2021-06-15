import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class A {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t-->0){
            int n = fs.nextInt();
            int m = fs.nextInt();
            char[][] grid = new char[n][m];
            char[][] aux1 = new char[n][m];
            char[][] aux2 = new char[n][m];
            for (int i = 0; i < n; i++) {
                char[] row = fs.next().toCharArray();
                grid[i] = row;
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if ((j+i)%2==0){
                        aux1[i][j]='W';
                        aux2[i][j]='R';
                    }else{
                        aux1[i][j]='R';
                        aux2[i][j]='W';
                    }
                }
            }
            int countA = 0;
            int countB = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (aux1[i][j]==grid[i][j]){
                        countA++;
                    }
                    if (aux2[i][j]==grid[i][j]){
                        countB++;
                    }
                }
            }
            System.out.println((countA!=0 && countB!=0)?"NO":"YES");
            if (countA==0 && countB!=0){
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        System.out.print(aux2[i][j]);
                    }
                    System.out.println();
                }
            }else if (countA!=0 && countB==0){
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        System.out.print(aux1[i][j]);
                    }
                    System.out.println();
                }
            }else if (countA==0 && countB==0){
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < m; j++) {
                        System.out.print(aux1[i][j]);
                    }
                    System.out.println();
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
