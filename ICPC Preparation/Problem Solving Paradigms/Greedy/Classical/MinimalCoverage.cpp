// https://onlinejudge.org/external/100/10020.pdf
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

bool cmp(pi a, pi b){
    if (abs(a.first-b.first)>EPS)return a.first<b.first;
    else return a.second>b.second;
    //return a.second > b.second;
}
int main(){
	Fast
	FastScanner fs;
	int t = fs.nextInt();
    while (t--){
        int l = fs.nextInt();
        vector<pair<int,int>> arr;
        while (true){

            int n = fs.nextInt();
            int m = fs.nextInt();
            if (!m && !n)break;
            if ((n<0 && m<0) || (n>l && m>l))continue;
            arr.push_back({n,m});
        }
        sort(arr.begin(), arr.end(), cmp);
        /*for (int i = 0; i < arr.size(); ++i) {
            cout<<arr[i].first<<" "<<arr[i].second<<endl;
        }*/
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
            cout<<0<<endl;
        }
        else{
            cout<<indexSolutions<<endl;
            for (int j = 0; j < indexSolutions; ++j) {
                cout<<solutions[j].first<<" "<<solutions[j].second<<endl;
            }
        }
        if (t){
            cout<<endl;
        }
        /*int f = 0;
        int start = 0;
        while(start<l)
        {
            int i;
            for (i=0;i<arr.size();i++)
            {
                if (arr[i].first <= start && arr[i].second > start)
                {
                    start = arr[i].second;   //Update interval
                    arr[f] = arr[i];
                    f++;
                    break;
                }
            }
            if (i==arr.size()) break;   //If there is no interval that meets the conditions, it ends directly.
        }
        if(start<l) printf("0\n");else {
            cout<<f<<endl;
            for (int i=0;i<f;i++)
                printf("%d %d\n", arr[i].first,arr[i].second);
        }
        if (t){
            cout<<endl;
        }*/

    }
	return 0;
}