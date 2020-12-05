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
    //In this case, the condition to search odd and even numbers
    int odd = count_if(v.begin(),v.end(),[](auto elem){ return elem %2!=0;}); //first way using v.method or member
    int evenNumbers = count_if(begin(v),end(v),[](auto elem){ return elem %2==0;});//second way using begin/end as a function or nonmember
    cout<<odd<<endl;
    cout<<evenNumbers<<endl;
}