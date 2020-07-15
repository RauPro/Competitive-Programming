#include <bits/stdc++.h>
using namespace std;
int main() {
    int t;cin>>t;
    while (t--){
        int x; long int k;
        cin>>x>>k;
        vector<long int > vector(x);
        for (int i = 0; i < x; ++i) {
            cin>>vector[i];
        }
        sort(vector.begin(),vector.end());
        int aux=0;
        long int cur=0;
        for (int j = x-1; j >= 0; j--) {
            cur++;
            if(vector[j] * cur >= k) {
                aux++;
                cur = 0;
            }
        }
        cout<<aux<<endl;
    }

    return 0;
}
