import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.StringTokenizer;

public class TrapezoidalRule {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		Scanner sc = new Scanner(System.in);
		double a = sc.nextDouble();
		double b = sc.nextDouble();
		int n = sc.nextInt();
		System.out.println(integrate(a,b,n));
    }

	static double f(double x) {
		//return Math.exp(- x * x / 2) / Math.sqrt(2 * Math.PI);
		return 1/(x+1);
	}


	static double integrate(double a, double b, int N) {
		double h = (b - a) / N;              // step size
		double sum = 0.5 * (f(a) + f(b));    // area
		for (int i = 1; i < N; i++) {
			double x = a + h * i;
			sum = sum + f(x);
		}

		return sum * h;
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
