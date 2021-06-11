import com.sun.javafx.UnmodifiableArrayList;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class TreeHeap {
	static int maxSize = 0;
	static int size = 5;
	//int[] heap = new int[5];
	static ArrayList<Integer> heap = new ArrayList<>();
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
		
    }
    static int parent( int index){
    	return (heap.get(index/2));
	}

	static int leftChild( int index){
		return (heap.get(2*index));
	}

	static int rightChild( int index){
		return (heap.get(2*index+1));
	}
	static void siftUp( int index){
    	while (index>1 && heap.get(parent( index))<heap.get(index)){
    		Collections.swap(heap, heap.get(parent( index)), heap.get(index));
    		index = parent( index);
		}
	}
	static void siftDown( int index){
		maxSize = index;
		int auxLeft = leftChild(index);
		if (auxLeft<=size && heap.get(auxLeft) > heap.get(maxSize)){
			maxSize = auxLeft;
		}
		int auxRight = rightChild(index);
		if (auxRight<=size && heap.get(auxRight)>heap.get(maxSize)){
			maxSize = auxRight;
		}
		if (index!=maxSize){
			Collections.swap(heap, heap.get(index), heap.get(maxSize));
			siftDown(maxSize);
		}
	}
	static void insert(int p){
    	if (size == maxSize){
			System.out.println("NO MORE TO ADD");
			return;
		}
    	heap.add(p);
    	siftUp(size);
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
