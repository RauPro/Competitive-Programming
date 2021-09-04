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

vi arr;
vi lengthAws;
vi p;
int LISAws = 0;
void length_LIS(int i) {                          // backtracking routine
    if (p[i] == -1) { LISAws+=lengthAws[i]; return; }// base case
    length_LIS(p[i]);                               // backtrack
    LISAws+=lengthAws[i];
}
int LIS(vi A, int n){
    //p.clear();
    int k = 0, lis_end = 0;
    vi L(n, 0), L_id(n, 0);
    p.assign(n, -1);

    for (int i = 0; i < n; ++i) {                  // O(n)
        int pos = lower_bound(L.begin(), L.begin()+k, A[i]) - L.begin();
        L[pos] = A[i];                               // greedily overwrite this
        L_id[pos] = i;                               // remember the index too
        p[i] = pos ? L_id[pos-1] : -1;               // predecessor info
        if (pos == k) {                              // can extend LIS?
            k = pos+1;                                 // k = longer LIS by +1
            lis_end = i;                               // keep best ending i
        }
    }
    for (int i = 0; i < p.size(); ++i) {
        cout<<p[i]<<" ";
    }cout<<endl;
    //cout<<lis_end<<endl;
    length_LIS(n-1);
    return k;
}
int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    for (int i = 1; i <= t; ++i) {
        LISAws = 0;
        int n = fs.nextInt();
        arr = fs.readArray(n);
        lengthAws = fs.readArray(n);
        for (int j = 0; j < n-1; ++j) {
            if (arr[j]==arr[j+1]){
                if (lengthAws[j]>lengthAws[j+1]){
                    lengthAws.erase(lengthAws.begin()+j+1);
                    arr.erase(arr.begin()+j+1);

                }else{
                    lengthAws.erase(lengthAws.begin()+j);
                    arr.erase(arr.begin()+j);

                }
                n--;
                j--;
            }
        }
        n = arr.size();
        for (int j = 0; j < n; ++j) {
            cout<<arr[j]<<" ";
        }cout<<endl;
        for (int j = 0; j < n; ++j) {
            cout<<lengthAws[j]<<" ";
        }cout<<endl;
        n = arr.size();
        //lengthAws = fs.readArray(n);*/
        int lis = LIS(arr, n);
        cout<<"Case "<<i;
        cout<<". Increasing ("<<LISAws<<"). ";
        reverse(arr.begin(), arr.end());
        reverse(lengthAws.begin(), lengthAws.end());
        LISAws = 0;
        int lds = LIS(arr, n);
        cout<<"Decreasing ("<<LISAws<<"). "<<endl;
        LISAws = 0;
    }
	return 0;
}