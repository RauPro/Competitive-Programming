#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define LSOne(S) ((S) & -(S)) // Useful bitmask operation
#define Fast ios::sync_with_stdio(0); cin.tie(0);
#define all(con) con.begin(),con.end()

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
	int t =fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        vi arr = fs.readArray(n);
        cout<<1<<" "<<1<<endl;
        //|ai−ak|+|ak−aj|=|ai−aj|
        /*sort(all(arr));
        bool aws = false;
        for (int i = 0; i < n; ++i) {
            int ai = arr[i];
            for (int j = i; j < n; ++j) {
                int aj = arr[j];
                for (int k = 0; k < n; ++k) {
                    int ak = arr[k];
                    if (abs(ai-ak) + abs(ak-aj) == abs(ai-aj)){
                        cout<< i+1 <<" "<<j+1<<endl;
                        aws = true;
                        break;
                    }
                }
                if (aws) break;;
            }
            if (aws) break;;
        }*/
    }
	return 0;
}