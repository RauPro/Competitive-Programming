import sun.reflect.generics.tree.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class C {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t-->0){
            int n = fs.nextInt();
            int l = fs.nextInt();
            int r = fs.nextInt();
            int[] arr = fs.readArray(n);
            TreeMap<Integer, Integer> treeMap = new TreeMap<>();
            for (int x : arr) {
                treeMap.put(x, -x);
            }
            int ix = 0;
            for (int x:treeMap.keySet()) {
                ix++;
                treeMap.put(x, ix);
            }

            FenwickTree bit = new FenwickTree(n+1);
            long aws = 0;
            for (int x:arr) {
                int from = treeMap.ceilingEntry(l - x).getValue();
                int to = treeMap.floorEntry(r - x).getValue();
                aws += bit.rsq(from, to);
                bit.update(treeMap.get(x), 1);
            }
            System.out.println(aws);
        }
    }
    static class FenwickTree {
        private ArrayList<Integer> ft;

        private int LSOne(int S) { return (S & (-S)); }

        public FenwickTree() {}

        // initialization: n + 1 zeroes, ignore index 0
        public FenwickTree(int n) {
            ft = new ArrayList<>();
            for (int i = 0; i <= n; i++) ft.add(0);
        }

        public int rsq(int j) {                              // returns RSQ(1, j)
            int sum = 0; for (; j > 0; j -= LSOne(j)) sum += ft.get(j);
            return sum; }

        public int rsq(int i, int j) {                       // returns RSQ(i, j)
            return rsq(j) - rsq(i-1); }

        // updates value of the i-th element by v (v can be +ve/inc or -ve/dec)
        void update(int i, int v) {                      // note: n = ft.size()-1
            for (; i < (int)ft.size(); i += LSOne(i)) ft.set(i, ft.get(i)+v); }
    };
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
