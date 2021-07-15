#include <bits/stdc++.h>
using namespace std;

#define Fast ios::sync_with_stdio(0); cin.tie(0);


typedef long long ll;
typedef long int li;
typedef vector<int> vi;
typedef vector<ll> vl;

int main(){
	Fast
	int n;
	int r;
    while (cin>>n && cin>>r){
        unordered_map<int,int> mapper;
        if(n==r){
            for (int i = 0; i <r; ++i) {
                int aux;cin>>aux;
            }
            cout<<"*"<<endl;
        }else{
            for (int i = 0; i <r; ++i) {
                int aux;cin>>aux;
                mapper[aux]=1;
            }
            for (int i = 1; i <= n; ++i) {
                if(!mapper[i]){
                    cout<<i<<" ";
                }
            }cout<<endl;
        }
    }
    return 0;
}