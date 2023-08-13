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
	//Fast
	FastScanner fs;
	int n = fs.nextInt();
    vector<string> arr;
    unordered_map<int, bool> hasLetter;
    for (int i = 0; i < n; ++i) {
        string e = fs.next();
        arr.push_back(e);
        hasLetter[e[0]] = true;
    }
    bool flag = false;
    for (int i = 0; i < n; ++i) { //O(n*m)
        int size = arr[i].size();
        int aws = 0;
        for (char j : arr[i]) {
            aws+= hasLetter[j]; // false = 0, true = 1
            if (aws == size){
                flag = true;
                break;
            }
        }
    }
    cout<< (flag ? "Y":"N")<<endl;
	return 0;
}