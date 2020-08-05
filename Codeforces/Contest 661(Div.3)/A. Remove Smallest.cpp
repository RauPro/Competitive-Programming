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
		int n;cin>>n;
		vi vector(n);
		for (int i=0;i<n;i++){
			cin>>vector[i];
		}
		sort(vector.begin(), vector.end());
		int p=0;
		if(abs(vector[0]-vector[n-1])<=1){
			vector[0]=vector[n-1];
		}
		for (int i=0;i<n-1;i++){
			if(abs(vector[i]-vector[i+1])>1){
				p++;		
				}
		}
		if (p>=1){
			cout<<"NO"<<endl;
		}
		else{
			cout<<"YES"<<endl;
		}
	}
} 
