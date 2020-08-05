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
		int x, y ,z;cin>>x>>y>>z;
		vi vector(3);
		vector[0]=x;
		vector[1]=y;
		vector[2]=z;
		sort(vector.begin(), vector.end());
		if (vector[1]==vector[2]){
			cout<<"YES"<<endl;
			cout<< vector[2]<<" "<<vector[1]<<" "<<vector[0]<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
} 
