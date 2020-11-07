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
		string s;cin>>s;
		int awns1=0;
		int awns0=0;
		for(int i=0;i<n-1;i++){
			if(s[i]==s[i+1] and s[i]=='1')awns1++;
			if(s[i]==s[i+1] and s[i]=='0')awns0++;
		}
		if(awns0==awns1)cout<<awns0<<endl;
		if(awns0>awns1)cout<<(awns0)<<endl;
		if(awns0<awns1)cout<<(awns1)<<endl;
	}
} 
