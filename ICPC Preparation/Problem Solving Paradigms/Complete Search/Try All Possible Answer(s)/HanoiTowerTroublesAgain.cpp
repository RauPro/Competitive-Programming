// https://onlinejudge.org/external/102/10276.pdf
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
bool isSqrt(int n){
    double s = sqrt(n);
    return (ceil(s)- floor(s)==0);
}

int main(){
	Fast
	FastScanner fs;
	int t  = fs.nextInt();
    while (t--){
        int n = fs.nextInt();
        vi pegs(n, 0);
        pegs[0]=1;
        int ball = 2;
        while (true){
            //ball++;
            bool done = true;
            int i = 0;
            while (i<n) {
                if (isSqrt(pegs[i]+ball) || pegs[i]==0){
                    //cout<<i<<" "<<ball<<" "<<pegs[i]+ball<<endl;
                    pegs[i]=ball;
                    done = false;
                    ball++;
                    i = 0;
                    continue;
                }
                i++;
            }
            if (done){
                cout<<ball-1<<endl;
                break;
            }
        }
    }
	return 0;
}