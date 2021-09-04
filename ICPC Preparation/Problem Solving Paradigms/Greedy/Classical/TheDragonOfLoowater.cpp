// https://open.kattis.com/problems/loowater

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
    while (true){
        int n = fs.nextInt();
        int m = fs.nextInt();
        if(!m && !n)break;
        vi heads = fs.readArray(n);
        vi knight = fs.readArray(m);
        sort(heads.begin(), heads.end());// sorting is an important
        sort(knight.begin(), knight.end());// pre-processing step
        int gold = 0, d=0,k=0;// both arrays are sorted
        while ((d < n) && (k < m)) {// while not done yet
            while ((k<m) && (heads[d]>knight[k]))k++;// find required knight k
            if (k == m) break;// loowater is doomed :S
            gold += knight[k];// pay this amount of gold
            ++d; ++k;// next dragon & knight
        }
        if (d == n) printf("%d\n", gold);// all dragons are chopped
        else        printf("Loowater is doomed!\n");
    }
	return 0;
}