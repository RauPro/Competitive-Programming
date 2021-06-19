import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.StringTokenizer;

public class TripleVariable {
	static double x1;
	static double x2;
	static double n;
	static double m;
	static double p;
    public static void main(String[] args) {
		Scanner fs = new Scanner(System.in);
		x1 = fs.nextDouble();
		x2 = fs.nextDouble();
		n = fs.nextDouble();
		m = fs.nextDouble();
		p = fs.nextDouble();
        System.out.println(integrate());
    }
    static double integrate(){
        double h = (x2-x1)/(n);
        double sum = ((double) 1/3) * (g(x1)+g(x2));
        // 4/3 terms
        for (int i = 1; i <= n - 1; i += 2) {
            double x = x1 + h * i;
            sum += 4.0 / 3.0 * g(x);
        }

        // 2/3 terms
        for (int i = 2; i < n - 1; i += 2) {
            double x = x1 + h * i;
            sum += 2.0 / 3.0 * g(x);
        }
        return sum*h;
    }
    static double g(double x){
        double k = (d(x)-c(x))/(m);
        double sum = ((double) 1/3) * (i(x,c(x))+i(x,d(x)));

        for (int i = 1; i <= m - 1; i += 2) {
            double y = c(x) + k * i;
            sum += 4.0 / 3.0 * i(x, y);
        }

        // 2/3 terms
        for (int i = 2; i < m - 1; i += 2) {
            double y = c(x) + k * i;
            sum += 2.0 / 3.0 * i(x, y);
        }
        //System.out.println(sum*k);
        return sum*k;
    }
    static double i(double x, double y){
        double j = (s(x,y)-e(x,y))/(m);
        double sum = ((double) 1/3) * (f(x,y, s(x, y))+f(x,y, e(x,y)));
        for (int i = 1; i <= m - 1; i += 2) {
            double z = e(x,y) + j * i;
            sum += 4.0 / 3.0 * f(x, y, z);
        }

        // 2/3 terms
        for (int i = 2; i < m - 1; i += 2) {
            double z = e(x,y) + j * i;
            sum += 2.0 / 3.0 * f(x, y, z);
        }
        return sum*j;
    }

    static double f(double x, double y, double z){
        return Math.pow(x, 2)+Math.pow(y, 2)+z;
    }
    static double c(double x){
        return x-1;
    }
    static double d(double x){
        return x+6;
    }
    static double e(double x, double y){
        return -2.0;
    }
    static double s(double x, double y){
        return 4+Math.pow(y,2);
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
