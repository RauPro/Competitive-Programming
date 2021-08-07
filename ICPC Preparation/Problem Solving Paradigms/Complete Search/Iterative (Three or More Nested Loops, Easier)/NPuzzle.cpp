// https://open.kattis.com/problems/npuzzle
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
	string rows[4];
	unordered_map<char, pi> mapper;
	mapper['A'] = {0 , 0};
    mapper['B'] = {0 , 1};
    mapper['C'] = {0 , 2};
    mapper['D'] = {0 , 3};
    mapper['E'] = {1 , 0};
    mapper['F'] = {1 , 1};
    mapper['G'] = {1 , 2};
    mapper['H'] = {1 , 3};
    mapper['I'] = {2 , 0};
    mapper['J'] = {2 , 1};
    mapper['K'] = {2 , 2};
    mapper['L'] = {2 , 3};
    mapper['M'] = {3 , 0};
    mapper['N'] = {3 , 1};
    mapper['O'] = {3 , 2};
    mapper['.'] = {3,3};
    int aws = 0;
    for (int i = 0; i < 4; ++i) {
        rows[i] = fs.next();
        string aux = rows[i];
        for (int j = 0; j < 4; ++j) {
            aws += abs(mapper[aux[j]].first-i)+abs(mapper[aux[j]].second-j);
        }
    }
    cout<<aws<<endl;
	return 0;
}