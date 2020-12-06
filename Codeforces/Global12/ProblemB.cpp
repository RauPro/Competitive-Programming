#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);

typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main(){
    Fast
    int t;cin>>t;
    while(t--){
        int n,k;cin>>n>>k;
        vector<pair<int,int>> cordenades;
        int x,y;
        for (int i = 0; i < n; ++i) {
            cin>>x>>y;
            cordenades.push_back(make_pair(x,y));
        }
        bool flag = true;
        for (int j = 0; j < n and flag; ++j) {
            for (int i = 0; i < n; ++i) {
                int aws = abs(cordenades[j].first-cordenades[i].first)+abs(cordenades[j].second-cordenades[i].second);
                if (aws>k){
                    flag=false;
                }
            }
        }
        if (flag){
            cout<<"1"<<endl;
        }else{
            cout<<"-1"<<endl;
        }
    }
}
