// The approach is correct but CPP dont have BigInt
// https://onlinejudge.org/external/7/787.pdf
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


int main(){
	Fast
	FastScanner fs;
	int first;
    while (cin>>first){
        vi arr;
        arr.push_back(first);
        while (true){
            int n = fs.nextInt();
            if (n==-999999)break;
            arr.push_back(n);
        }
        vi prod;
        ll sum = 1, ans = -1e6;
        for (int i = 0; i < arr.size(); ++i) {
            sum = arr[i];
            for (int j = i+1; j < arr.size(); ++j) {
                sum*=arr[j];
                ans = max(ans, sum);                         // keep the cur max RSQ
            }
            //if (sum <= 0) sum = 1;                        // reset the running sum
        }
        cout<<(arr.size()==1?arr[0]:ans)<<endl;
    }
	return 0;
}