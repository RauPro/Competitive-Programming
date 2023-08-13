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
	int n = fs.nextInt();
	int k = fs.nextInt();
	vector<pair<int, int>> arr;
	int minE = INT32_MAX;
	int maxE = INT32_MAX * (-1);
    for (int i = 0; i < n; ++i) {
        int e = fs.nextInt();
        arr.push_back({e, i+1});
        minE = min(minE, e);
        maxE = max(maxE, e);

    }
    sort(arr.begin(), arr.end());
    /*for (int i = 0; i < n; ++i) {
        cout<< "Value: "<<arr[i].first<<" Index:"<< arr[i].second<<endl;
    }*/
    int aws = arr[k-1].first;
    if (k==0){
        cout<<(arr[k].first==1?-1:arr[k].first-1)<<endl;
    }
    else if (aws != arr[k].first){
        cout<<aws<<endl;
    }else{
        cout<<-1<<endl;
    }
	return 0;
}