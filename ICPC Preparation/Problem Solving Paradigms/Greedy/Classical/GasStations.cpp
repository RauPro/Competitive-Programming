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
typedef vector<pi> vp;

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

bool cmp(pi a, pi b){
    if (abs(a.first-b.first)>EPS)return a.first<b.first;
    else return a.second>b.second;
    //return a.second > b.second;
}

int main(){
	Fast
	FastScanner fs;
    while (true){
        int l = fs.nextInt();
        int g = fs.nextInt();
        if (!l && !g)break;
        vp arr;
        for(int i = 0; i< g;i++){
            int x = fs.nextInt();
            int r = fs.nextInt();
            arr.push_back({x-r, x+r});
        }
        sort(arr.begin(), arr.end(), cmp);
        vector<pi> solutions(arr.size());

        int xDone = 0;
        int i = 0;
        int indexSolutions = 0;

        while (i < arr.size() && xDone < l){
            solutions[indexSolutions].second = 0;
            while (arr[i].first <= xDone && i < arr.size()){
                if (arr[i].second > solutions[indexSolutions].second){
                    solutions[indexSolutions] = arr[i];
                }
                i++;
            }
            if (solutions[indexSolutions].second == xDone)break;
            xDone = solutions[indexSolutions].second;
            indexSolutions++;
        }
        if (xDone < l){
            cout<<-1<<endl;
        }
        else{
            cout<<g-indexSolutions<<endl;

        }

    }
	return 0;
}
