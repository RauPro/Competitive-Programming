import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t = fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            int m = fs.nextInt();
            int aws =0;
            char[][] matix = new char[n][m];
            for (int i = 0; i < n; i++) {
                char [] line = fs.next().toCharArray();
                for (int j = 0; j < m; j++) {
                    matix[i][j]=line[j];
                    //if (line[j]=='*')aws++;
                }
            }
            int[][] auxMatrix = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (matix[i][j]=='*'){
                        auxMatrix[i][j]=1;
                    }
                    else {
                        auxMatrix[i][j]=0;
                    }
                }
            }
            for (int i = n - 2; i >= 0; i--) {
                for (int j = 0; j < m; j++) {
                    if (auxMatrix[i][j] > 0) {
                        if (j - 1 >= 0 && j + 1 < m) {
                            boolean flag = true;
                            int minCases = auxMatrix[i + 1][j - 1];
                            for (int x = j - 1; x <= j + 1; x++) {
                                minCases = Math.min(minCases, auxMatrix[i + 1][x]);
                                if (auxMatrix[i + 1][x] <= 0) {
                                    flag = false;
                                    break;
                                }
                            }
                            if (flag) {
                                auxMatrix[i][j] = minCases + 1;
                            }
                        }
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    aws += auxMatrix[i][j];
                }
            }
            System.out.println(aws);
            t--;
        }
    }
    static class FastScanner {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer("");
        String next() {
            while (!st.hasMoreTokens())
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
        int[] readauxMatrixay(int n) {
            int[] a=new int[n];
            for (int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
