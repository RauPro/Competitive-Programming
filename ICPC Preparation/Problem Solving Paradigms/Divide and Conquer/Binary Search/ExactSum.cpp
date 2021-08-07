// https://onlinejudge.org/external/110/11057.pdf
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
	int n;
    while (cin>>n){
        vi arr = fs.readArray(n);
        sort(arr.begin(), arr.end());
        int m = fs.nextInt();
        int newM = m - arr[0];
        int element = arr[0];
        pi pairAws;
        int minAws = m;
        for (int i = 0; i < arr.size(); ++i) {
            auto priceMatch = lower_bound(arr.begin(), arr.end(), newM);
            int index = priceMatch- arr.begin();
            if (arr[index]==newM && abs(newM - element)<=minAws){
                minAws = (newM-element);
                pairAws.first = newM;
                pairAws.second = element;

            }
            newM = m - arr[i];
            element = arr[i];
        }
        cout<<"Peter should buy books whose prices are "<<min(pairAws.first, pairAws.second)<<" and "<<max(pairAws.first, pairAws.second)<<"."<<endl;
        cout<<endl;
    }
	return 0;
}