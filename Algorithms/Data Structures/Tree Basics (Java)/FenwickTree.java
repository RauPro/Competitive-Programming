import java.util.ArrayList;

public class FenwickTree {
    private ArrayList<Integer> ft;

    private int LSOne(int S) {
        return (S & (-S));
    }

    public FenwickTree() {
    }

    // initialization: n + 1 zeroes, ignore index 0
    public FenwickTree(int n) {
        ft = new ArrayList<>();
        for (int i = 0; i <= n; i++) ft.add(0);
    }

    public int rsq(int j) {                              // returns RSQ(1, j)
        int sum = 0;
        for (; j > 0; j -= LSOne(j)) sum += ft.get(j);
        return sum;
    }

    public int rsq(int i, int j) {                       // returns RSQ(i, j)
        return rsq(j) - rsq(i - 1);
    }

    // updates value of the i-th element by v (v can be +ve/inc or -ve/dec)
    void update(int i, int v) {                      // note: n = ft.size()-1
        for (; i < (int) ft.size(); i += LSOne(i)) ft.set(i, ft.get(i) + v);
    }
}
