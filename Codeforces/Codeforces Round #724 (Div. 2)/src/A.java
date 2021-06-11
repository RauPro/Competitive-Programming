import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class A {

    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
        	int n = fs.nextInt();
        	int[] arr = fs.readArray(n);
            ArrayList<Integer> tree = new ArrayList<>();
            int aws = 0;
            boolean flag = false;
            for (int i = 0; i < n; i++) {
                if (arr[i]<0){
                    aws++;
                }
                tree.add(arr[i]);
            }
            for (int i = 0; i < tree.size(); i++) {
                for (int j = 0; j < tree.size(); j++) {
                    if (i!=j){
                        if (tree.contains(Math.abs(tree.get(i)-tree.get(j)))){
                            continue;
                        }else if (tree.size()==300){
                            flag = true;
                            break;
                        }
                        else{
                            tree.add(Math.abs(tree.get(i)-tree.get(j)));
                        }
                    }
                }

            }

            if (aws>1 || flag){
                System.out.println("NO");
            }
            else{
                System.out.println("YES");
                System.out.println(tree.size());
                for (int d:tree
                     ) {
                    System.out.print(d+" ");
                }
                System.out.println();
            }
			t--;
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
