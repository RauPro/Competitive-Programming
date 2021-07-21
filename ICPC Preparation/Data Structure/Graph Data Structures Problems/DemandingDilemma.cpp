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


int main(){
	Fast
	int t;cin>>t;
    while (t--){
        int n;cin>>n;
        int m;cin>>m;
        vi conected(m, 0);
        int incidenceMatrix[n][m];
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                cin>>incidenceMatrix[j][k];
                if(incidenceMatrix[j][k]==1){
                    conected[k]++;
                }
            }
        }
       vi hashMapped(500, 0);
        for (int j = 0; j < n; ++j) {
            int dop = 0;
            int auxAcum = 0;
            for (int k = 0; k < m; ++k) {
                if(incidenceMatrix[k][j]==1){
                    dop+=k;
                    auxAcum++;
                }
            }
            if (auxAcum==2)hashMapped[dop]++;

        }
        bool flagGraph = false;
        for (const auto &item : hashMapped) {
            if(item>=2 && m!=1){
                flagGraph=true;
                break;
            }
        }
        int aws= 0;
        for (int j = 0; j < conected.size(); ++j) {
            if(conected[j]==2)aws++;
        }
        if (aws == m && !flagGraph)cout<<"Yes"<<endl;
        else cout<<"No"<<endl;

    }
	return 0;
}
