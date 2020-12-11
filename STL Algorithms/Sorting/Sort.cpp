#include <bits/stdc++.h>
using namespace std;
#define Fast ios::sync_with_stdio(0); cin.tie(0);
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
void show(vi v){
    for (auto i:v ){
        cout<<i<<" ";
    }
    cout<<endl;
}
int main(){
    Fast
    vi v{2,7,8,3,4,10,5,7};
    //it is false rn
    cout<<is_sorted(v.begin(),v.end())<<endl;
    //Sort default is element1<element2
    sort(v.begin(),v.end());
    show(v);
    //now is true
    cout<<is_sorted(v.begin(),v.end())<<endl;
    //modify sorting default element1>element2
    sort(v.begin(),v.end(),[](int element1,int element2){ return element1>element2;});
    show(v);
    vi v2{2,7,8,3,4,10,5,7};
    partial_sort(v2.begin(),find(v.begin(),v.end(),10),v2.end());
    show(v2);

    //shuffle is the method to unshort
}