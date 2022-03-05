// 10116 - Robot Motion
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
        int p = fs.nextInt();
        if (!n && !m && !p)break;
        int auxGraph[n][m];
        memset(auxGraph, 0, sizeof auxGraph);
        vector<string> matrix(n);
        for (int i = 0; i < n; ++i) {
            matrix[i] = fs.next();
        }
        int indexGraph = 1;
        int y = 0;
        int x = p-1;
        bool flagCorrect = false;
        while (auxGraph[y][x]==0){
            auxGraph[y][x] = indexGraph;
            indexGraph++;
            //cout<<matrix[y][x]<<endl;
            if (matrix[y][x]=='N'){
                y--;
            }
            else if (matrix[y][x]=='S'){
                y++;
            }
            else if (matrix[y][x]=='E'){
                x++;
            }
            else if (matrix[y][x]=='W'){
                x--;
            }
            if (x<0 || x>=m || y<0 || y>=n){
                flagCorrect = true;
                break;
            }
        }

        if (flagCorrect){
            cout<<indexGraph-1<<" step(s) to exit"<<endl;
        }else{
            cout<<auxGraph[y][x]-1<< " step(s) before a loop of "<< indexGraph- (auxGraph[y][x]) <<" step(s)"<<endl;
        }
    }
	return 0;
}