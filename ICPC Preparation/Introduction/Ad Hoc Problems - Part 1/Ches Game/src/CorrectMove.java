import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class CorrectMove {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNextInt()) {
            char[][] arr = new char[8][8];
            int king = sc.nextInt();
            int queen = sc.nextInt();
            int movements = sc.nextInt();
            if (king == queen) {
                System.out.println("Illegal state");
                continue;
            }
            for (int i = 0; i < 8; i++)
                for (int j = 0; j < 8; j++)
                    arr[i][j] = 'e';
            int r = king / 8;
            int c = king - r * 8;
            arr[r][c] = 'k';
            if (r + 1 < 8)
                arr[r + 1][c] = 'o';
            if (r - 1 >= 0)
                arr[r - 1][c] = 'o';
            if (c + 1 < 8)
                arr[r][c + 1] = 'o';
            if (c - 1 >= 0)
                arr[r][c - 1] = 'o';

            r = queen / 8;
            c = queen - r * 8;
            arr[r][c] = 'q';
            for (int i = r; i < 8 && arr[i][c] != 'k'; i++) {

                if (arr[i][c] == 'o')
                    arr[i][c] = 'g';
                else
                    arr[i][c] = 'x';
            }
            for (int i = r; i >= 0 && arr[i][c] != 'k'; i--) {
                if (arr[i][c] == 'o')
                    arr[i][c] = 'g';
                else
                    arr[i][c] = 'x';
            }
            for (int i = c; i < 8 && arr[r][i] != 'k'; i++) {
                if (arr[r][i] == 'o')
                    arr[r][i] = 'g';
                else
                    arr[r][i] = 'x';
            }
            for (int i = c; i >= 0 && arr[r][i] != 'k'; i--) {
                if (arr[r][i] == 'o')
                    arr[r][i] = 'g';
                else
                    arr[r][i] = 'x';
            }
            r = queen / 8;
            c = queen - r * 8;
            arr[r][c] = 'q';
            int y = movements / 8;
            int x = movements - y * 8;
            if (arr[y][x] == 'g')
                System.out.printf("Move not allowed\n");
            else if (arr[y][x] != 'x')
                System.out.printf("Illegal move\n");
            else if (arr[y][x] == 'x') {
                if (movements == 49 && king == 56 || movements == 14 && king == 7 || movements == 9 && king == 0 || movements == 54 && king == 63)
                    System.out.printf("Stop\n");
                else
                    System.out.printf("Continue\n");
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
