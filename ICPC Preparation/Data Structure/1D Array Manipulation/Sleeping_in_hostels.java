import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// UVa 13181 - Sleeping in hostels
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=5092
public class Sleeping_in_hostels {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()){
            char[] s = sc.nextLine().toCharArray();
            ArrayList<Integer> aux = new  ArrayList<>();
            int x=0,y=0;
            boolean flagA = false,flagB=false;
            for (char c : s) {
                //System.out.println(c=='.');
                if (c == '.') {
                    x++;
                } else {
                    aux.add(x);
                    x = 0;
                }
            }
            aux.add(x);
            y= Collections.max(aux);
            //System.out.println(aux);
            aux.set(0,aux.get(0)-1);
            aux.set(aux.size()-1,aux.get(aux.size()-1)-1);

            for (int i = 1; i < aux.size()-1; i++) {
                if (aux.get(i)%2==0){
                    aux.set(i,(aux.get(i)/2)-1);
                }else {
                    aux.set(i,(aux.get(i)/2));
                }
            }
            System.out.println(Collections.max(aux));
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
