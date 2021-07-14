import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;
// UVa 12503 - Robot Instructions
// https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3947
public class RobotInstructions {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t!=0){
            int n = sc.nextInt();
            ArrayList<String> instructions = new ArrayList<>();
            int aws = 0;
            sc.nextLine();
            for (int i = 0; i < n; i++) {
                String in = sc.nextLine();

                instructions.add(in);
                if (in.equals("LEFT"))aws--;
                if(in.equals("RIGHT"))aws++;
            }

            for (String data:instructions) {
                String[] d = data.split("\\s+");
                if (d[0].equals("SAME")){
                    int ans = Integer.parseInt(d[2]);
                    while (!instructions.get(ans-1).equals("LEFT") && !instructions.get(ans-1).equals("RIGHT")){
                        ans= Integer.parseInt(instructions.get(ans-1).split("\\s+")[2]);
                    }
                    if (instructions.get(ans-1).equals("LEFT"))aws--;
                    if (instructions.get(ans-1).equals("RIGHT"))aws++;
                }
            }
            System.out.println(aws);
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
