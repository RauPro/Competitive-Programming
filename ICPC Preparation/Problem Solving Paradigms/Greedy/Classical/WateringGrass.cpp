// https://onlinejudge.org/external/103/10382.pdf
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

const double EPS = 1e-9;

// Sweep Line
struct sp{
    int x, r;
    double x_l,x_r;
};

sp sprinkler[10010];

bool cmp(sp a, sp b){
    if (fabs(a.x_l-b.x_l)>EPS)return a.x_l<b.x_l;
    else return a.x_r>b.x_r;
}

int main(){
	Fast
	FastScanner fs;
    int n, l, w;
    while (cin>>n && cin>>l && cin>>w){
        for (int i = 0; i < n; ++i) {
            sprinkler[i].x = fs.nextInt();
            sprinkler[i].r = fs.nextInt();
            if(2*sprinkler[i].r>=w){
                double d_x = sqrt((double)sprinkler[i].r*sprinkler[i].r - (w/2.0)*(w/2.0));
                sprinkler[i].x_l = sprinkler[i].x-d_x; // sort based on smaller x_l and then larger x_r
                sprinkler[i].x_r = sprinkler[i].x+d_x;
            }else
                sprinkler[i].x_l = sprinkler[i].x_r = sprinkler[i].x; // to make this unselected...
        }
        sort(sprinkler, sprinkler+n, cmp); // sort sprinklers by range x_l x_r
        /*for (int i = 0; i < n; ++i) {
            cout<<sprinkler[i].x_l<<" "<<sprinkler[i].x_r<<endl;
        }
        cout<<(1+EPS)<<"ENP"<<endl;*/
        bool possible = true;
        double covered = 0.0;
        int ans = 0;
        for (int i = 0; (i < n) && possible; ++i) {
            if (covered>l)break;// done
            if (sprinkler[i].x_r<(covered+EPS))continue;// inside prev interval
            if (sprinkler[i].x_l<(covered+EPS)){// can cover
                double max_r = -1.0;
                int max_id;
                for (int j = i; (j < n) && (sprinkler[j].x_l<(covered+EPS)); ++j) {
                    if (sprinkler[j].x_r>max_r){ //go to right to find
                        max_r = sprinkler[j].x_r; // interval with
                        max_id = j; // largest coverage
                    }
                }
                ++ans;
                covered = max_r; // jump here
                i = max_id;
            }else{
                possible = false;
            }

        }
        if (!possible || (covered < l))cout<<-1<<"\n";
        else cout<<ans<<"\n";

    }
	return 0;
}