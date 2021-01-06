import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class D {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        int t= fs.nextInt();
        while (t!=0){
            int n = fs.nextInt();
            List<Long> evenNumbers = new ArrayList<>(n);
            List<Long> oddNumbersNumbers = new ArrayList<>(n);
            for (int i = 0; i < n; i++) {
                long a = fs.nextLong();
                if (a % 2 == 0) {
                    evenNumbers.add(a);
                } else {
                    oddNumbersNumbers.add(a);
                }
            }
            evenNumbers.sort(Comparator.naturalOrder());
            oddNumbersNumbers.sort(Comparator.naturalOrder());

            int x = 1;

            int oddNumbersNumbersR = oddNumbersNumbers.size() - 1;
            int evenNumberstR = evenNumbers.size() - 1;
            long awsAlice = 0;
            long awsBob = 0;


            while (oddNumbersNumbersR >= 0 || evenNumberstR >= 0) {
                long lastevenNumbers = 0;
                if (evenNumberstR >= 0) {
                    lastevenNumbers = evenNumbers.get(evenNumberstR);
                }
                long lastoddNumbersNumbers = 0;
                if (oddNumbersNumbersR >= 0) {
                    lastoddNumbersNumbers = oddNumbersNumbers.get(oddNumbersNumbersR);
                }

                if (x == 1) {
                    if (lastevenNumbers > lastoddNumbersNumbers) {
                        awsAlice += lastevenNumbers;
                        evenNumberstR--;
                    } else {
                        oddNumbersNumbersR--;
                    }
                    x = 2;
                } else {
                    if (lastoddNumbersNumbers > lastevenNumbers) {
                        awsBob += lastoddNumbersNumbers;
                        oddNumbersNumbersR--;
                    } else {
                        evenNumberstR--;
                    }
                    x = 1;
                }
            }

            if (awsAlice > awsBob) {
                System.out.println("Alice");
            } else if (awsBob > awsAlice) {
                System.out.println("Bob");
            } else {
                System.out.println("Tie");
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
