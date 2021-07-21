#include <bits/stdc++.h>
#include <bits/extc++.h> // pbds

using namespace std;
using namespace __gnu_pbds;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ost;
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pi;

vi readArray(int n){vi arr(n);for(int i = 0; i < n; ++i)cin>>arr[i];return arr;}

int main(){
	Fast
	int n;int m;
    while (cin>>n){
        cin>>m;
        vi arr(n);
        vector<pi> graph;
        vi hashOccurences(1000000, 0);
        for (int i = 0; i < n; ++i) {
            cin>>arr[i];
            hashOccurences[arr[i]]++;
            graph.push_back({arr[i], hashOccurences[arr[i]]});
        }
        bool flag = true;
        for (int i = 0; i < m; ++i) {
            flag = true;
            int k;cin>>k;
            int d;cin>>d;
            for (int j = 0; j < n; ++j) {
                if(k == graph[j].second && d == graph[j].first){
                    cout<<j+1<<"\n";
                    flag = false;
                    break;
                }
            }
            if(flag){
                cout<<"0"<<"\n";
            }
        }
    }
	return 0;
}
