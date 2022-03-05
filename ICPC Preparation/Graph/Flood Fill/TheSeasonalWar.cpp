// 352 - The Seasonal War
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
string grid[25];

int R, C;

int dr[] = { 1, 1, 0,-1,-1,-1, 0, 1};            // the order is:
int dc[] = { 0, 1, 1, 1, 0,-1,-1,-1};            // S/SE/E/NE/N/NW/W/SW

int floodfill(int r, int c, char c1, char c2) {  // returns the size of CC
    if ((r < 0) || (r >= R) || (c < 0) || (c >= C)) return 0; // outside grid
    if (grid[r][c] != c1) return 0;                // does not have color c1
    int ans = 1;                                   // (r, c) has color c1
    grid[r][c] = c2;                               // to avoid cycling
    for (int d = 0; d < 8; ++d)
        ans += floodfill(r+dr[d], c+dc[d], c1, c2);  // the code is neat as
    return ans;                                    // we use dr[] and dc[]
}

int main(){
	Fast
	FastScanner fs;
	int n;
	int t = 0;
    while (cin>>n){
        t++;
        for (int i = 0; i < n; ++i) {
            grid[i] = fs.next();
        }
        int aws = 0;
        R = C = n;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if(grid[i][j]=='1'){
                    aws++;
                    floodfill(i, j, '1', '.');
                }
            }
        }
        cout<<"Image number "<< t <<" contains " <<aws<< " war eagles."<<endl;
    }
	return 0;
}
