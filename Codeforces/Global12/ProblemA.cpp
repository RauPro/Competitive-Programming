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
        int n;cin>>n;
        string s;cin>>s;
        vector<char> v(n);
        for (int i = 0; i < n; ++i) {
            v[i]=s[i];
        }
        sort(v.begin(),v.end());
        for (int i = 0; i < n; ++i) {
            cout<<v[i];
        }
        cout<<endl;
    }
} 