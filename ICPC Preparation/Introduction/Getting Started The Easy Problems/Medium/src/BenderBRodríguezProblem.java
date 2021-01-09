import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 11507 - Bender B. Rodríguez Problem
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2502
public class BenderBRodríguezProblem {
    static boolean strcmp(String a1,String a2){
        return !a1.equals(a2);
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        String [] aws = new String[]{"+x","-x","+y","-y","+z","-z"};
        while (true){
            int n = fs.nextInt();
            if (n==0)break;
            String[] arr = new String[n-1];
            for (int i = 0; i < arr.length; i++) {
                arr[i]=fs.next();
            }
            int direction = 0;
            for (int i = 0; i < arr.length; i++) {
                if(!strcmp(arr[i], "No"))
                    continue;
                if(!strcmp(arr[i], "+z")) {
                    if(direction == 0)        direction = 4;
                    else if(direction == 1)   direction = 5;
                    else if(direction == 4)   direction = 1;
                    else if(direction == 5)   direction = 0;
                }
                if(!strcmp(arr[i], "-z")) {
                    if(direction == 0)        direction = 5;
                    else if(direction == 1)   direction = 4;
                    else if(direction == 4)   direction = 0;
                    else if(direction == 5)   direction = 1;
                }
                if(!strcmp(arr[i], "+y")) {
                    if(direction == 0)        direction = 2;
                    else if(direction == 1)   direction = 3;
                    else if(direction == 2)   direction = 1;
                    else if(direction == 3)   direction = 0;
                }
                if(!strcmp(arr[i], "-y")) {
                    if(direction == 0)        direction = 3;
                    else if(direction == 1)   direction = 2;
                    else if(direction == 2)   direction = 0;
                    else if(direction == 3)   direction = 1;
                }
            }
            System.out.println(aws[direction]);
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
