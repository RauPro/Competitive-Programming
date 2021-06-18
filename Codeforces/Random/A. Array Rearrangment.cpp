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
		int a,b;cin>>a>>b;
		vi vectorA(a);
		vi vectorB(a);
		for(int i=0;i<a;i++){
			cin>>vectorA[i];
		}
		for(int i=0;i<a;i++){
			cin>>vectorB[i];
		}
		int awns=0;
		for(int i=0;i<a;i++){
			if(vectorA[i]+vectorB[a-1-i]>b){
				awns++;
			}
		}
		if(awns==0){
			cout<<"YES"<<endl;
		}else{
			cout<<"NO"<<endl;
		}
	}
} 
