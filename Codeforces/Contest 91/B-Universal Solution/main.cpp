#include <bits/stdc++.h>
using namespace std;
typedef vector<int> v;
int main() {
    int t;cin>>t;
    while(t--){
        char value='R';
        v vector(3);
        string s;cin>>s;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i]=='R'){
                vector[0]++;
            }
            else if(s[i]=='S'){
                vector[1]++;
            }
            else if(s[i]=='P'){
                vector[2]++;
            }
        }
        int aux=0;
        for (int i = 0; i < 3; ++i) {
            if (vector[i]>vector[aux]){
                aux=i;
            };
        }
        if(aux==0) value='P';
        else if(aux==1) value='R';
        else if(aux==2) value='S';
        for (int j = 0; j < s.size(); ++j) {
            cout<<value;
        }
        cout<<endl;
    }
    return 0;
}
