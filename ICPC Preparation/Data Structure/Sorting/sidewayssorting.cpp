#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main(){
    Fast
    while (true){
        int n; cin>>n;
        int r; cin>>r;
        if(!r && !n){
            break;
        }
        for (size_t i = 0; i < n; i++) {
            string s; cin>>s;
            sort(s.begin(), s.end(),[](const char a, const char b){
                return toupper(a)<toupper(b);
            });
            cout<<s<<endl;
        }
        cout<<endl;
    }
    
} 