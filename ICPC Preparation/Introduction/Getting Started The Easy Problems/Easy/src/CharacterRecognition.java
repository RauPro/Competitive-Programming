import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 12658 - Character Recognition?
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=4396
public class CharacterRecognition {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();
        char[][] arr = new char[5][1000];
        int len = 0;
        for (int i = 0; i < 5; i++) {
            String data = fs.next();
            arr[i] = data.toCharArray();
            len = data.length();
        }
        test: for (int i = 0; i < len; i++) {
            if (arr[3][i] == '*') {
                try {
                    if (arr[3][i] == '*' && arr[1][i + 2] == '*') {
                        System.out.print(2);
                    } else if (arr[3][i] == '*' && arr[1][i] == '*' && arr[0][i - 1] == '*') {
                        System.out.print(3);
                        continue test;
                    }
                } catch (ArrayIndexOutOfBoundsException e) {
                    if (arr[0][i] == '*' && arr[1][i] == '*' && arr[2][i] == '*' && arr[3][i] == '*' && arr[4][i] == '*') {
                        System.out.print(1);
                    }
                    continue test;
                }
                if (arr[0][i] == '*' && arr[1][i] == '*' && arr[2][i] == '*' && arr[3][i] == '*' && arr[4][i] == '*') {
                    System.out.print(1);
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
