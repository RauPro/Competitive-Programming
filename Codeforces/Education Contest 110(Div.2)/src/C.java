import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class C {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		while (t!=0){
			char[] arr = fs.next().toCharArray();
			//naive way
			/*Deque<Integer> aux =new LinkedList<>();
			boolean flag = false;
			for (int i = 0; i < arr.length; i++) {
				if (arr[i]=='?'){
					aux.push(i);
					flag = true;
				}
				if ((arr[i]=='1' || arr[i]=='0') && flag){
					changedSrt(arr, aux, arr[i]);
					flag = false;

				}
			}
			}*/
			long aws = 0;
			long size1 = 0;
			long size0 = 0;
			for (char c:arr) {
				long x = (c == '0' || c == '?')? size0 + 1: 0;
				long y = (c == '1' || c == '?')? size1 + 1: 0;
				size1 = x;
				size0 = y;
				aws += Math.max(size1, size0);
			}
			System.out.println(aws);
			t--;
		}
    }
	static void changedSrt(char[] arr, Deque<Integer> aux, char status){
		if (aux.size()!=0){
			arr[aux.getFirst()]= counter(status);
			aux.pop();
			changedSrt(arr, aux, counter(status));
		}
	}
	static char counter(char n){
    	return n=='1'?'0':'1';
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
