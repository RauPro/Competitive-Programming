// https://onlinejudge.org/external/114/11402.pdf  I got wa and pe
#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ll> vll;
typedef pair<int, int> pi;

class FastScanner{
public:
	int nextInt(){int a;cin>>a;return a;}
    char nextChar(){char a;cin>>a;return a;}
    ll nextLong(){ll a;cin>>a;return a;}
    string next(){string a;cin>>a;return a;}
    vi readArray(int n){
		vi a(n);
		for (size_t i = 0; i < n; i++)cin>>a[i];
		return a;}
};

class SegmentTree {                              // OOP style
private:
  int n;                                         // n = (int)A.size()
  vi A, st, lazy;                                // the arrays

  int l(int p) { return  p<<1; }                 // go to left child
  int r(int p) { return (p<<1)+1; }              // go to right child

  int conquer(int a, int b) {
    if (a == -1) return b;                       // corner case
    if (b == -1) return a;
    return min(a, b);                            // RMQ
  }

  void build(int p, int L, int R) {              // O(n)
    if (L == R)
      st[p] = A[L];                              // base case
    else {
      int m = (L+R)/2;
      build(l(p), L  , m);
      build(r(p), m+1, R);
        st[p] = st[l(p)] + st[r(p)];
    }
  }

  void propagate(int p, int L, int R) {
      if (lazy[p] == -1) return;
      if (lazy[p] == 1) {
          st[p] = R - L + 1;
      } else if (lazy[p] == 0) {
          st[p] = 0;
      } else if (lazy[p] == 2) {
          st[p] = (R - L + 1 - st[p]);
      }

      if (R != L) {
          if (lazy[p] < 2) {
              lazy[l(p)] = lazy[r(p)] = lazy[p];
          } else {
              lazy[l(p)] = flip(lazy[l(p)]);
              lazy[r(p)] = flip(lazy[r(p)]);
          }
      }

      lazy[p] = -1;
  }
    int RSQ(int p, int L, int R, int i, int j, int depth = 0) {
        propagate(p, L, R);

        if (i > j) return 0;
        if (L >= i && R <= j) return st[p];
        int m = (L + R) / 2;

        return RSQ(l(p), L, m, i, min(m, j), depth + 1) + RSQ(r(p), m + 1, R, max(m + 1, i), j, depth + 1);
    }
  int RMQ(int p, int L, int R, int i, int j) {   // O(log n)
    propagate(p, L, R);                          // lazy propagation
    if (i > j) return -1;                        // infeasible
    if ((L >= i) && (R <= j)) return st[p];      // found the segment
    int m = (L+R)/2;
    return conquer(RMQ(l(p), L  , m, i          , min(m, j)),
                   RMQ(r(p), m+1, R, max(i, m+1), j        ));
  }

  void update(int p, int L, int R, int i, int j, int val) { // O(log n)
    propagate(p, L, R);                          // lazy propagation
    if (i > j) return;
    if ((L >= i) && (R <= j)) {                  // found the segment
         lazy[p] = val;                             // update this
      propagate(p, L, R);                        // lazy propagation
    }
    else {
      int m = (L+R)/2;
      update(l(p), L  , m, i          , min(m, j), val);
      update(r(p), m+1, R, max(i, m+1), j        , val);
        st[p] = st[l(p)] + st[r(p)];
    }
  }
    int flip(int x) {
        return 1 - x;
    }
  void show(){
      for (int i = 0; i < st.size(); ++i) {
          cout<<st[i]<<" ";
      }cout<<endl;
  }

public:
  SegmentTree(int sz) : n(sz), st(4*n), lazy(4*n, -1) {}

  SegmentTree(const vi &initialA) : SegmentTree((int)initialA.size()) {
    A = initialA;
    build(1, 0, n-1);
  }

  void update(int i, int j, int val) { update(1, 0, n-1, i, j, val); }
    int RSQ(int i, int j) {
        return RSQ(1, 0, n - 1, i, j);
    }
  int RMQ(int i, int j) { return RMQ(1, 0, n-1, i, j); }
  void showSt(){ show(); };
};

int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
	int cas = 0;
    while (t--){
        cout<<"Case "<<++cas<<": "<<endl;
        int n = fs.nextInt();
        string st = "";
        while (n--){
            int m = fs.nextInt();
            string s = fs.next();
            for (int i = 0; i < m; ++i) {
                st+=s;
            }
        }
        vi arr;
        for (int i = 0; i < st.length(); ++i) {
            arr.push_back((st[i])-48);
        }
        SegmentTree segmentTree(arr);
        int q = fs.nextInt();
        int query = 0;
        for (int j = 1; j <= q; ++j) {
            char action = fs.nextChar();
            int a = fs.nextInt();
            int b = fs.nextInt();
            if (action == 'F'){
                segmentTree.update(a,b, 1);
            }
            if (action == 'E'){
                segmentTree.update(a,b, 0);
            }
            if (action == 'I'){
                segmentTree.update(a,b,2);
            } if (action == 'S'){
                cout<<"Q"<<++query<<": "<<segmentTree.RSQ(a, b)<<endl;
            }
        }
    }
	return 0;
}