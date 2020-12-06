#include <bits/stdc++.h>
using namespace std;
#define Fast ios::sync_with_stdio(0); cin.tie(0);
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
int main(){
    Fast
    vi v{2,7,8,3,4,10,5,7};
    //Find the fist number two
    auto findProof = find(v.begin(),v.end(),10); //save reference of the finding
    int results = findProof-v.begin(); //get the index of the value
    cout<<results<<endl;
}