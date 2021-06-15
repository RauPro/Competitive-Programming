import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class B {
    static class Pair implements Comparable<Pair> {
        Integer _first, _second;

        public Pair(Integer f, Integer s) {
            _first = f;
            _second = s;
        }

        public int compareTo(Pair o) {
            if (!this.first().equals(o.first()))
                return this.first() - o.first();
            else
                return this.second() - o.second();
        }

        Integer first() { return _first; }
        Integer second() { return _second; }
    }
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t-->0){
            int n=fs.nextInt();
            ArrayList<Long> nums = new ArrayList<>();
            nums.add(0L);
            for (int i = 0; i < n; i++) {
                long x = fs.nextLong();
                nums.add(x);
            }
            nums.add(0L);

            long value = 0;
            for (int i = 0; i <= n; i++) {
                value += Math.abs(nums.get(i) - nums.get(i+1));
            }

             long counter = 0, aws = 0;
            for (int i = 1; i <= n; i++) {
                counter = Math.min((nums.get(i) - nums.get(i-1)), (nums.get(i) - nums.get(i+1)));
                if (counter > 0) aws += counter;
            }
            System.out.println(value - aws);
        }
    }
    static int getCost(int[] arr){
        int cost = arr[0];
        for (int i = 1; i < arr.length; i++) {
            cost+= Math.abs(arr[i]-arr[i-1]);
        }
        cost+=arr[arr.length-1];
        return cost;
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
