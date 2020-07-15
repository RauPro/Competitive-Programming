#include <bits/stdc++.h>
using namespace std;
typedef vector<int> v;

int main() {

    int t;cin>>t;
    while (t--){
        bool status= true;
        int n;cin>>n;
        v vector(n);
        for (int i=0;i<n;i++){
            cin>>vector[i];
        }
        for (int i=0;i<n;i++){
            int b=-1 , a=-1;
            for (int j = 0; j < i ; ++j) {
                if (vector[j]<vector[i]){
                   b = j;
                }
            }
            for (int k = i+1; k < n; ++k) {
                if (vector[k]<vector[i]){
                    a = k;
                }
            }
            if (b>=0 and a>=0){
                status= false;
                cout<<"YES"<<endl;
                cout<<b+1<<" "<<i+1<<" "<<a+1<<endl;
                break;
            }
        }
        if (status){
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
