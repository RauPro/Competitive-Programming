#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

#include <random>

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
	vector<string> myvector = {"1-5",
            "6-11",
            "12-16",
            "17-22"};
    shuffle( myvector.begin(), myvector.end() , std::mt19937(std::random_device()()));
    cout<<"Raul: "<<myvector[0]<<endl;
    cout<<"Emely: "<<myvector[1]<<endl;
    cout<<"Mayi: "<<myvector[2]<<endl;
    cout<<"Kevin: "<<myvector[3]<<endl;

    return 0;
}