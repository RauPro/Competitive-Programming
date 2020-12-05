#include <bits/stdc++.h>
using namespace std;
#define Fast ios::sync_with_stdio(0); cin.tie(0);
typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;
int main(){
    Fast
    vi v{1,2,2,3,4,5,5,7};
    //Target used is two, but you can add the number that you want to count
    int two=count(v.begin(),v.end(),2); //first way using v.method or member
    int twoSecondWay=count(begin(v),end(v),1);//second way using begin/end as a function or nonmember
    cout<<two<<endl;
    cout<<twoSecondWay<<endl;
}