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
		int a,b,c,d;cin>>a>>b>>c>>d;
		cout<<(max(a+b,c+d))<<endl;
	}
} 
