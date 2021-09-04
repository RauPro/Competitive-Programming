// https://open.kattis.com/problems/froshweek2
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
	int m = fs.nextInt();
    vi task = fs.readArray(n);
    vi music = fs.readArray(m);
    sort(task.begin(), task.end());// sorting is an important
    sort(music.begin(), music.end());// pre-processing step
    int aws=0, i =0, j=0;
    while ((i < n) && (j < m)){
        while ((j<m) && (task[i]>music[j]))j++;// find required knight k
        if (j == m) break;// loowater is doomed :S
        aws++;
        ++i; ++j;// next dragon & knight

    }
    cout<<aws<<endl;
	return 0;
}