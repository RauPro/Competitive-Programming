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
/*
 * 0000
 * 0001
 * 0010
 * 0011*/

string arrayToString(vi list){
    string s;
    for (int i = 0; i < list.size(); ++i) {
        s += to_string(list[i]);
    }
    return s;
}
unordered_map<string, bool> mapper;
void permutation(vi list, int diff){

    if (count(list.begin(), list.end(), 1) == diff){
        //printArray(list);
        string s;
        for (int i = 0; i < list.size(); ++i) {
            s += to_string(list[i]);
        }
        cout<<s<<endl;
        mapper[s] = true;
    }
    for (int i = list.size()-1; i >= 0 ; --i) {
        if (list[i]==1){
            list[i] = 0;
        }else{
            list[i] = 1;
            if (mapper[arrayToString(list)]) continue;
            permutation(list, diff);
        }
    }
}

int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){

        int length = fs.nextInt();
        int diff = fs.nextInt();
        const int l = 17;
        //vi list;
        //list.assign(length,0);
        //permutation(list, diff);
        int decimal = pow(2,length);
        decimal--;
        int ans = 0;
        for (int i = 0; i < pow(2,length); ++i) {
            if (diff == __builtin_popcount(ans)){
                string s = bitset<l>(ans).to_string();
                cout<<s.substr(17-length,length)<<endl;
            }
            if (ans == decimal){
                break;
            }
            ans++;
        }
        if(t)cout<<endl;
    }
	return 0;
}